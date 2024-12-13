from random import choices
from string import ascii_letters

from django.test import TestCase
from django.urls import reverse

from shopapp.models import Product
from shopapp.utils import add_two_numbers



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


