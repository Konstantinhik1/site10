from itertools import product
from random import choices
from string import ascii_letters

import self
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from shopapp.models import Product
from shopapp.utils import add_two_numbers



from django.contrib.auth.models import User
from django.conf import settings

class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result=add_two_numbers(2, 3)
        self.assertEqual(result, 5)




class ProductCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def test_create_product(self):
        # Добавляем заголовок HTTP_USER_AGENT
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": self.product_name,
                "price": "123.45",
                "description": "A good table",
                "discount": "10"
            },
            HTTP_USER_AGENT="TestAgent/1.0"
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )






class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()  # Важно вызывать super() для базовой инициализации
        # Создаем тестовый продукт
        cls.product = Product.objects.create(name="Best Product")

    @classmethod
    def tearDownClass(cls):
        # Удаляем тестовый продукт
        cls.product.delete()
        super().tearDownClass()

    def test_get_product_and_check_content(self):
        # Добавляем заголовок HTTP_USER_AGENT в запрос
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk}),
            HTTP_USER_AGENT="TestAgent/1.0"
        )
        # Проверяем статус кода ответа
        self.assertContains(response,self.product.name )


#
# class ProductsListViewTestVase(TestCase):
#     fixtures = [
#         'products-fixture.json',
#     ]
#
#     def test_products(self):
#         response = self.client.get(reverse("shopapp:products_list"), HTTP_USER_AGENT='TestAgent/1.0')
#
#         self.assertEqual(
#             list(Product.objects.filter(archived=False).values_list('pk', flat=True)),
#             [p.pk for p in response.context["products"]],
#         )
#         self.assertTemplateUsed(response, "shopapp/products-list.html")







class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.credentials = dict(username="Kostya_test", password="qwerty")
        cls.user = User.objects.create_user(**cls.credentials)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()

    def setUp(self):
        self.client.login(**self.credentials)

    def test_orders_view(self):
        # Test for an authenticated user with HTTP_USER_AGENT
        response = self.client.get(reverse("shopapp:orders_list"), HTTP_USER_AGENT='TestAgent/1.0')
        self.assertContains(response, "Orders")

    def test_orders_view_not_authenticated(self):
        # Test for a not authenticated user, expects a redirect to the login page
        self.client.logout()
        response = self.client.get(reverse("shopapp:orders_list"))

        # Check for a 302 redirect status
        self.assertEqual(response.status_code, 302)

        # Check if the redirect URL matches the LOGIN_URL
        self.assertIn(str(settings.LOGIN_URL), response.url)


# Убедитесь, что импорт правильный

from django.test import TestCase
from django.urls import reverse
from shopapp.models import Product  # Импортируем модель Product

class ProductsExportViewTestCase(TestCase):
    # Загружаем фикстуру данных для теста
    fixtures = [
        'products-fixture.json',  # Убедитесь, что путь к фикстуре корректен
    ]

    def test_get_products_view(self):
        # Отправляем GET-запрос к представлению
        response = self.client.get(reverse("shopapp:products_export"))  # Используем правильное имя маршрута
        self.assertEqual(response.status_code, 200)  # Проверяем, что статус ответа 200 (OK)

        # Получаем данные из базы данных
        products = Product.objects.order_by("pk").all()

        # Создаем список ожидаемых данных, приводя цену к типу float
        expected_data = [
            {
                "pk": product.pk,  # ID продукта
                "name": product.name,  # Название продукта
                "price": float(product.price),  # Преобразуем цену в float для согласованности с представлением
            }
            for product in products
        ]

        # Получаем JSON-данные из ответа
        products_data = response.json()

        # Проверяем, что данные из ответа совпадают с ожидаемыми
        self.assertEqual(
            products_data["products"],
            expected_data,
        )
