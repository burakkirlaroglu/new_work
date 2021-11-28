from django.db import models

from django.contrib.auth.models import User
from blog_modules.post.models import Post
from blog_modules.base.models import  StartModel

class Favourite(StartModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username
