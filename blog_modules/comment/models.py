from django.db import models
from blog_modules.base.models import StartModel
from django.contrib.auth.models import User

from blog_modules.post.models import Post


class Comment(StartModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='replies')

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return self.post.title + " " + self.user.username

    def save(self, *args, **kwargs):
        return super(Comment, self).save(*args, **kwargs)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def any_children(self):
        return Comment.objects.filter(parent=self).exists()
