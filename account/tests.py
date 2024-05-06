from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from account.views import RegisterView, ActivationView


class TestUrls(SimpleTestCase):
    def test_register_url_is_resolved(self):
        url = reverse("register")
        view = resolve(url).func.view_class
        self.assertEqual(view, RegisterView)

    def test_activate_view_is_resolved(self):
        url = reverse("activate", kwargs={"email": "admin2@admin.com", "activation_code": "1234567890"})
        view = resolve(url).func.view_class
        self.assertEqual(view, ActivationView)


class TestViews(TestCase):
    def test_register_view(self):
        response = self.client.post(reverse("register"), data={
            "email": "example@gmail.com",
            "password": "1234",
            "password_confirm": "1234"
        })
        self.assertEqual(response.status_code, 201)

    def test_activation_view(self):
        response = self.client.get(reverse("activate",kwargs={"email": "admin2@admin.com", "activation_code": "1234567890"}))
        self.assertEqual(response.status_code, 200)
