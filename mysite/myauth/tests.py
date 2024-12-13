import json

from django.template.context_processors import request
from django.test import TestCase
from django.urls import reverse

class GetCookieViewTestCase(TestCase):
    def test_get_cookie_view(self):
        # Установим заголовок HTTP_USER_AGENT
        response = self.client.get(
            reverse("myauth:cookie-get"),
            HTTP_USER_AGENT="TestAgent/1.0"
        )
        self.assertContains(response, "Cookie value")


class FooBarViewTest(TestCase):
    def test_foo_bar_view(self):
        # Установим заголовок HTTP_USER_AGENT
        response = self.client.get(
            reverse("myauth:foo-bar"),
            HTTP_USER_AGENT="TestAgent/1.0"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.headers['content-type'], 'application/json',
        )
        expected_data = {"foo": "bar", "spam": "eggs"}
        # Распарсим JSON-ответ
        response_data = json.loads(response.content)
        self.assertEqual(response_data, expected_data)

