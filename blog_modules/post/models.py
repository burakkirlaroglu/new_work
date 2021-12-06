from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    slug = models.SlugField(unique=True, editable=False)
    image = models.ImageField(upload_to="media/post", null=True, blank=True)
    modeified_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, related_name='modified_by')

    """
    editable false dendiği zaman güncelleme vs işlemleri yapılırken bu fieldlar
    gözükmez false değeri true yapılırsa ki default değeri true dur o zaman
    o fieldlar görünür olur ve değiştirilebilir"""


    class Meta:
        ordering = ('-id',)

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        new_slug = slug
        number = 1
        while Post.objects.filter(slug=new_slug).exists():
            new_slug = "{}-{}".format(slug, number)
            number += 1
        return new_slug

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)
