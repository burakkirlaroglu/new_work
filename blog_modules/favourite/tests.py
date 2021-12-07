from rest_framework.test import APITestCase
from django.urls import reverse


class FavouriteAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.fav_url = reverse("favourite:create-list")

    def test_add_fav_success(self):
        pass



