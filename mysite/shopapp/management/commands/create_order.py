from collections.abc import Sequence

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from shopapp.models import Order, Product  # Убедитесь, что Order импортирован из вашего models.py


class Command(BaseCommand):
    @ transaction.atomic
    def handle(self, *args, **options):

        self.stdout.write("Create order with products")

        # Получаем пользователя с именем 'admin'
        user = User.objects.get(username="admin")
        # products:Sequence[Product] = Product.objects.defer("description", "price","created_at").all()
        products: Sequence[Product] = Product.objects.only("id").all()

        # Создаем заказ или получаем существующий
        order, created = Order.objects.get_or_create(
            delivery_address="ul Ivanova, d 8",
            promocode="promo5",
            user=user,
        )
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(f"Created order {order}")
