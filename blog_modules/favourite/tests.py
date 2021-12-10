import json

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from blog_modules.favourite.models import Favourite
from blog_modules.post.models import Post


class FavouriteAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.fav_url = reverse("favourite:create-list")
        self.login_url = reverse("token_obtain_pair")
        self.username = "testuser"
        self.password = "test12340"
        self.user = User.objects.create_user(username=self.username,
                                             password=self.password)
        self.user_2 = User.objects.create_user(username="ikinciuser",
                                               password="ikincipass1234")
        self.post = Post.objects.create(user=self.user, content="içerik",
                                        title="başlık")
        self.post_2 = Post.objects.create(user=self.user, content="içerik",
                                          title="başlık")
        self.fav_2 = Favourite.objects.create(content="hımm güzel",
                                              user=self.user_2,
                                              post=self.post_2)
        self.test_jwt_auth_success()

    def test_jwt_auth_success(self):
        response = self.client.post(path=self.login_url,
                                    data={"username": self.username,
                                          "password": self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_list_fav(self):
        self.test_add_fav_success()
        response = self.client.get(self.fav_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Favourite.objects.count(), 2)
        self.assertEqual(Favourite.objects.filter(user=self.user.id).count(),
                         1)
        self.assertEqual(Favourite.objects.filter(user=self.user_2.id).count(),
                         1)

    def test_add_fav_success(self):
        data = {
            "content": "favlı içerik",
            "user": self.user.id,
            "post": self.post.id
        }
        response = self.client.post(self.fav_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], data.get('content'))
        self.assertEqual(response.data['user'], data.get('user'))
        self.assertEqual(response.data['post'], data.get('post'))

    def test_delete_fav(self):
        fav = Favourite.objects.create(content="asd",
                                       user=self.user,
                                       post=self.post_2)
        self.del_up_fav_url = reverse("favourite:delete-update",
                                      kwargs={"pk": fav.id})
        response = self.client.delete(self.del_up_fav_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Favourite.objects.count(), 1)

    def test_update_fav(self):
        fav = Favourite.objects.create(content="asd",
                                       user=self.user,
                                       post=self.post_2)
        new_data = {
            "content": "güncel veri"
        }
        self.del_up_fav_url = reverse("favourite:delete-update",
                                      kwargs={"pk": fav.id})
        response_before = self.client.get(self.del_up_fav_url)
        self.assertEqual(response_before.data, {"content": "asd"})

        response = self.client.put(self.del_up_fav_url, data=new_data,
                                   format="json")
        self.assertEqual(response.data['content'], new_data['content'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
