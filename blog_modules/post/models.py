from django.db import models
from blog_modules.base.models import StartModel
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(StartModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(unique=True, editable=False)
    media = models.ImageField(upload_to="media/posts/", null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True
                                    , related_name="modified_by")

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        new_slug = slug
        number = 1
        while Post.objects.filter(slug=new_slug).exists():
            new_slug = "{}-{}".format(slug, number)
            number += 1
        return new_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)
