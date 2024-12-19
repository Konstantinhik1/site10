from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductDetailsView,
    ProductsListView,
    OrdersListView,
    OrderDetailView,
    create_product,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsDataExportView,
    ProductViewSet,
)

app_name = "shopapp"

routers = DefaultRouter()
routers.register("products",ProductViewSet)

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("api/", include(routers.urls)),
    path("groups/",GroupsListView.as_view(), name="groups_list"),
    path("products/",ProductsListView.as_view(), name="products_list"),
    path("products/export/", ProductsDataExportView.as_view(),name = "products_export"),  # Здесь имя маршрута "products_export"
    path("products/create",  ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update/",ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/confirm-delete/",ProductDeleteView.as_view(), name="product_delete"),
    path("products/create/", create_product, name="product_create"),
    path("orders/",  OrdersListView.as_view(), name="orders_list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),

]


