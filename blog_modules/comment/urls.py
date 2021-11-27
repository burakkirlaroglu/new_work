from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from blog_modules.comment.resources.views import (CommentApiViews,
                                                  CommentListApiView)

urlpatterns = [
    path('comment/', CommentApiViews.as_view()),
    path('comment/all/', CommentListApiView.as_view()),
]
