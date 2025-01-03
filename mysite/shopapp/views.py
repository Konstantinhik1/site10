"""
В этом модуле лежат различные наборы представлений.

Разные view интернет-магазина: по товарам, заказам и т.д.
"""
from timeit import default_timer

import logging
from django.contrib.admindocs.views import ViewIndexView
from django.contrib.auth.models import Group
from django.contrib.messages import success
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import  LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .forms import ProductForm , GroupForm
from .models import Product, Order
from rest_framework.viewsets import ModelViewSet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from timeit import default_timer
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiResponse


log = logging.getLogger(__name__)


@extend_schema(description="Product views CRUD")
class ProductViewSet(ModelViewSet):
    """
    набор представлений для действий для Product
    Полный CRUD сущностей товара
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name", "description"]
    filterset_fields =[
        "name",
        "description",
        "price",
        "discount",
    ]
    ordering_fields = [
        "name",
        "price",
        "discount",
    ]

    @extend_schema(
        summary="Get one product by ID",
        description="Retrieves **product**, returns 404 if not found",
        responses={
            200: ProductSerializer,
            404: OpenApiResponse(description="Empty response, product by id not found"),
        }
    )
    def retrieve(self,  *args, **kwargs):
        return super().retrieve(*args,**kwargs)

class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            "time_running": default_timer(),
            "products": products,
            "items": 1,
        }
        log.debug("Products for shop index: %s", products)
        log.info("Rendering shop index")
        return render(request, 'shopapp/shop-index.html', context=context)

class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm(),
            "groups": Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request:HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)

class ProductDetailsView(DetailView):
    template_name = "shopapp/products-details.html"
    # model = Product
    queryset = Product.objects.prefetch_related("images")
    context_object_name = "product"




class ProductsListView(ListView):
    template_name = "shopapp/products-list.html"
    model = Product
    context_object_name = "products"
    # queryset = Product.objects.filter(archived=False)

class ProductCreateView(UserPassesTestMixin,CreateView):
    def test_func(self):
        return self.request.user.groups.filter(name="secret-group").exists()
        # return self.request.user.is_superuser

    model = Product
    fields = "namme", "price", "description", "discount", "preview"
    success_url = reverse_lazy("shopapp:products_list")

class  ProductUpdateView(UpdateView):
    model = Product
    fields = "name", "price", "description", "discount", "preview"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "shopapp:product_details",
            kwargs={"pk": self.object.pk},
        )

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    # def form_valid(self, form):
    #     success_url =self.get_success_url()
    #     # self.object.archived = True
    #     self.object.save()
    #     return HttpResponseRedirect(success_url)




class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
        .all()
    )

class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "shopapp.view_order"
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )





class ProductsDataExportView(View):
    def get(self, request):
        # Получаем все продукты, сортируя их по первичному ключу
        products = Product.objects.order_by("pk").all()

        # Создаем список данных о каждом продукте
        products_data = [
            {
                "pk": product.pk,  # ID продукта
                "name": product.name,  # Название продукта
                "price": float(product.price),  # Преобразуем цену в тип float
            }
            for product in products
        ]

        # Возвращаем данные в формате JSON
        return JsonResponse({"products": products_data})


# Ensure this import is correct and the form exists

def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data["name"]
            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse("shopapp:products_list")  # Исправлено
            return redirect(url)
    else:
         form = ProductForm()  # Initialize the form
    context = {
        "form": form,
    }
    return render(request, "shopapp/create-product.html", context=context)






