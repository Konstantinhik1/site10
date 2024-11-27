from django.core.management import BaseCommand
from shopapp.models import Product

class Command(BaseCommand):
    """
    Create products
    """
    def handle(self, *args, **options):
        self.stdout.write("Creating products...")

        products_name = [
            "Laptop",
            "Desktop",
            "Smartphone",
        ]

        for product_name in products_name:
            product, created = Product.objects.get_or_create(name=product_name)

            if created:
                self.stdout.write(f"Created product: {product.name}")
            else:
                self.stdout.write(f"Product {product.name} already exists.")

        self.stdout.write(self.style.SUCCESS("Products creation process finished"))
