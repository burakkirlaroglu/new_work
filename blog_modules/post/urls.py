from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from blog_modules.post.resources.views import PostListViews, PostDetailApiView, PostDeleteApiView, PostUpdateApiView, PostCreateApiView

urlpatterns = [
    path('post/', PostListViews.as_view(), name='post-list'),
    path('post/<slug>/', PostDetailApiView.as_view(), name='post-detail'),
    path('post/update/<slug>/', PostUpdateApiView.as_view(), name='post-update'),
    path('post/delete/<slug>/', PostDeleteApiView.as_view(), name='post-delete'),
    path('create/', PostCreateApiView.as_view(), name='post-create')
]