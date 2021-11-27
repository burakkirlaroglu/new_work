from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from blog_modules.post.resources.views import PostListViews, PostDetailApiView, PostDeleteApiView, PostUpdateApiView, PostCreateApiView

urlpatterns = [
    path('post/', PostListViews.as_view()),
    path('post/<slug>/', PostDetailApiView.as_view(), name='detail'),
    path('post/update/<slug>/', PostUpdateApiView.as_view(),),
    path('post/delete/<slug>/', PostDeleteApiView.as_view(),),
    path('create/', PostCreateApiView.as_view(),)
]