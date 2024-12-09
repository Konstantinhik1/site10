from timeit import default_timer
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import ProductForm
from .forms import ProductForm
from .models import Product, Order

def shop_index(request: HttpRequest):
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

def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)

def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),  # Исправлена опечатка "prodducts"
    }
    return render(request, 'shopapp/products-list.html', context=context)

 # Ensure this import is correct and the form exists

def create_product(request: HttpRequest) -> HttpResponse:
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
