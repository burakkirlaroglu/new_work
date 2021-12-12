import json

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from blog_modules.comment.models import Comment
from blog_modules.post.models import Post


class CommentTestCase(APITestCase):

    def setUp(self) -> None:
        self.comment_url = reverse_lazy("comment:create")
        self.comment_list_url = reverse_lazy("comment:list")
        self.login_url = reverse_lazy("token_obtain_pair")
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
        self.test_jwt_auth_success()

    def test_jwt_auth_success(self):
        response = self.client.post(path=self.login_url,
                                    data={"username": self.username,
                                          "password": self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_comment_post_success(self):
        data = {
            "user": self.user.pk,
            "post": self.post.pk,
            "content": "kontente",
            "parent": ""
        }
        response = self.client.post(self.comment_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_list(self):
        self.assertEqual(Comment.objects.count(), 0)
        self.test_comment_post_success()
        response = self.client.get(self.comment_list_url)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_update(self):
        data = {
            "user": self.user,
            "post": self.post,
            "content": "kontente",
            "parent": None
        }
        comment = Comment.objects.create(**data)
        new_data = {
            "content": "yeni yorum"
        }
        comment_update_url = reverse_lazy("comment:update",
                                          kwargs={"pk": comment.pk})
        response = self.client.put(comment_update_url, data=new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_delete(self):
        data = {
            "user": self.user,
            "post": self.post_2,
            "content": "kontente",
            "parent": None
        }
        comment = Comment.objects.create(**data)
        comment_delete_url = reverse_lazy("comment:update",
                                          kwargs={"pk": comment.pk})
        self.assertEqual(Comment.objects.all().count(), 1)
        response = self.client.delete(comment_delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.all().count(), 0)
