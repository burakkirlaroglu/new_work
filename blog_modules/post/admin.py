from django.contrib import admin
from blog_modules.post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


admin.site.register(Post, PostAdmin)
