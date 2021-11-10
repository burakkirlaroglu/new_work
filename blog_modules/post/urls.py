from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from blog_modules.post.resources.views import PostListViews


urlpatterns = [
    path('post/', PostListViews.as_view(),)
]