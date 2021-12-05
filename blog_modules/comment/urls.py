from django.urls import path
from blog_modules.comment.resources.views import (CommentCreateApiViews,
                                                  CommentListApiView,
                                                  CommentUpdateApiView)

app_name = 'comment'
urlpatterns = [
    path('create', CommentCreateApiViews.as_view(), name='create'),
    path('list', CommentListApiView.as_view(), name='list'),
    # path('delete/<pk>', CommentDeleteApiView.as_view(), name='delete'),
    path('update/<pk>', CommentUpdateApiView.as_view(), name='update'),
]
