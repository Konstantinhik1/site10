from timeit import default_timer

from django.contrib.admindocs.views import ViewIndexView
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.views.generic import TemplateView

from .forms import ProductForm , GroupForm
from .models import Product, Order

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from timeit import default_timer

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
        }
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

class ProductDetailsView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        product = get_object_or_404(Product, pk=pk)
        context = {
            "product": product,
        }
        return render(request, 'shopapp/products-details.html', context=context)

class ProductsListView(TemplateView):
    template_name = "shopapp/products-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] =Product.objects.all()
        return context






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




def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),

    }
    return render(request, 'shopapp/orders-list.html', context=context)
