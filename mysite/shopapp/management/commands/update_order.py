from django.core.management import BaseCommand

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Получаем первый заказ
        order = Order.objects.first()  # Исправлено с 'object' на 'objects'
        if not order:
            self.stdout.write("No order found")
            return

        # Получаем все продукты
        products = Product.objects.all()  # Исправлено с 'object' на 'objects'

        # Добавляем продукты к заказу
        for product in products:
            order.products.add(product)

        order.save()  # Сохраняем изменения в заказе

        # Выводим сообщение о добавленных продуктах
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added products {[product.name for product in order.products.all()]} to order {order.id}"
            )
        )
