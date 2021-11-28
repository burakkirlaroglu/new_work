from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from blog_modules.comment.resources.views import (CommentApiViews,
                                                  CommentListApiView,
                                                  CommentDestroyApiView,
                                                  CommentUpdateApiView)

urlpatterns = [
    path('comment/', CommentApiViews.as_view(), name='comment-create'),
    path('comment/all/', CommentListApiView.as_view(),
         name='comment-list-all'),
    # path('comment/delete/<pk>/', CommentDestroyApiView.as_view()),
    path('comment/update/<pk>/', CommentUpdateApiView.as_view(),
         name='comment-update'),
]
