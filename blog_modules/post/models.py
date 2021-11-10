from django.db import models
from blog_modules.base.models import StartModel
from django.contrib.auth.models import User


class Post(StartModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
