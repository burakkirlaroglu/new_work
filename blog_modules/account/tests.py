import json

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class ProfileModelTestCase(APITestCase):

    def _login_token(self):
        self.test_successfully_registered()
        user_credentials = {
            "username": "test",
            "password": "12345678aklsjdlas"
        }
        response = self.client.post(self.token_url, user_credentials)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(token))

    def setUp(self) -> None:
        self.url = reverse("account:register")
        self.token_url = reverse("token_obtain_pair")
        self.password_change_url = reverse("account:change-password")
        self.user_me_url = reverse("account:me")

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
        user_credentials = {
            "username": "test",
            "password": "12345678aklsjdlas"
        }
        response = self.client.post(self.token_url, user_credentials)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(token))
        response_2 = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_403_FORBIDDEN)

    def test_login_successfully(self):
        User.objects.create_user(username="test", password="test1234")
        response = self.client.post(self.token_url, {"username": "test",
                                                     "password": "test1234"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response, "access")
        self.assertTrue(response, "refresh")

    def test_login_invalid_credentials(self):
        User.objects.create_user(username="test", password="test1234")
        response = self.client.post(self.token_url, {"username": "asdas",
                                                     "password": "test1234"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_blank_credentials(self):
        response = self.client.post(self.token_url, {"username": "",
                                                     "password": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_is_user_authenticated(self):
        response = self.client.get(self.password_change_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_is_password_change_valid_credentials(self):
        self.test_successfully_registered()
        user_credentials = {
            "username": "test",
            "password": "12345678aklsjdlas"
        }
        response = self.client.post(self.token_url, user_credentials)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(token))
        data = {
            "old_password": "12345678aklsjdlas",
            "new_password": "deneme1234"
        }
        response_2 = self.client.put(self.password_change_url, data)
        self.assertEqual(response_2.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_me_success(self):
        self._login_token()
        response = self.client.get(self.user_me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_info(self):
        self._login_token()
        data = {
            "first_name": "asd",
            "profile": {
                "note": "ddd",
                "twitter": "bbb"
            },
            "username": "denemeuser"
        }

        response = self.client.get(self.user_me_url)
        assert_data_f = json.loads(response.content)

        self.assertEqual(response.data['first_name'], "")
        self.assertEqual(response.data['username'], "test")
        self.assertEqual(assert_data_f['profile']['note'], "")
        self.assertEqual(assert_data_f['profile']['twitter'], "")

        response2 = self.client.put(self.user_me_url, data=data, format='json')

        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        assert_data = json.loads(response2.content)
        self.assertEqual(response2.data['first_name'], "asd")
        self.assertEqual(response2.data['username'], "denemeuser")
        self.assertEqual(assert_data['profile']['note'], "ddd")
        self.assertEqual(assert_data['profile']['twitter'], "bbb")
