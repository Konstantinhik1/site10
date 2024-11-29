from django.contrib import admin
from django.contrib.gis.gdal.field import Field

from .models import Product, Order

class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    list_display = "pk","name", "description_short", "price", "discount"  #"archived"
    list_display_links = "pk", "name"
    ordering ="-name", "pk"
    search_fields = "name", "description"
    fieldsets = [
        (None, {
            "fields": ("name", "description"),
        }),
        ("Price options", {
            "fields": ("price", "discount"),
            "classes": ("collapse", "wide"),
        })
        # ("Extra options",{
        #     "fields": ("archived",),
        #     "classes": ("colapse",),
        #     "description": "Extra options.Field 'archived' is for soft delete",
        # })

    ]

    def description_short(self,obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."

# admin.site.register(Product, ProductAdmin)

# class ProductInline(admin.TabularInline):
class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "delivery_address", "promocode", "created_at", "user"

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self,obj: Order) -> str:
        return obj.user.first_name or obj.user.username


