from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ProfileModelTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = reverse("account:register")

    def test_successfully_registered(self):
        user_credentials = {
            "username": "test",
            "password": "12345678aklsjdlas"
        }
        response = self.client.post(self.url, user_credentials)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user_credentials.get('username'), "test")
        self.assertEqual(user_credentials.get('password'), "12345678aklsjdlas")

    def test_invalid_password_registered(self):
        user_credentials = {
            "username": "test",
            "password": "1234"
        }
        response = self.client.post(self.url, user_credentials)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(response.data)

    def test_register_fail(self):
        self.test_successfully_registered()

        user_credentials = {
            "username": "test",
            "password": "12345678aklsj"
        }
        response = self.client.post(self.url, user_credentials)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"username": [
            "A user with that username already exists."
        ]})

    def test_already_account(self):
        self.test_successfully_registered()
        """header gönderip o şekilde test edilmesi lazım şimdilik 405 olarak
        kalacaktır."""
        self.client.login(username="test", password="12345678akl")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
