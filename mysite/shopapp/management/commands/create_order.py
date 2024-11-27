from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shopapp.models import Order  # Убедитесь, что Order импортирован из вашего models.py


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create order")

        # Получаем пользователя с именем 'admin'
        user = User.objects.get(username="admin")  # Ошибка была в "users", должно быть "user"

        # Создаем заказ или получаем существующий
        order, created = Order.objects.get_or_create(
            delivery_address="ul Pupkina, d8",
            promocode="SALE123",
            user=user,
        )
        self.stdout.write(f"Created order {order}")
