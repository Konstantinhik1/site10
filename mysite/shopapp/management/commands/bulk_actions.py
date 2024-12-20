from collections.abc import Sequence
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from shopapp.models import Order, Product  # Убедитесь, что Order импортирован из вашего models.py


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Start demo bulk actions")

        result= Product.objects.filter(
            name__contains="Smartphone",
        ).update(discount=10)

        print(result)

        # info = [
        #     ('Smartphone 1', 199),
        #     ('Smartphone 2', 299),
        #     ('Smartphone 3', 399),
        # ]
        #
        # # Создание объектов Product
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        #
        # # Исправлено: правильное обращение к менеджеру модели (Product.objects, а не Product.object)
        # result = Product.objects.bulk_create(products)
        #
        # # Печать созданных объектов
        # for obj in result:
        #     print(obj)

        self.stdout.write("Done")


