from django.urls import path
from blog_modules.post.resources.views import PostListViews, PostDetailApiView, \
    PostUpdateApiView, PostCreateApiView
from django.views.decorators.cache import cache_page

app_name = 'post'
urlpatterns = [
    path('list', cache_page(60 * 1)(PostListViews.as_view()), name='list'),
    path('detail/<pk>', PostDetailApiView.as_view(), name='detail'),
    # path('delete/<pk>', PostDeleteApiView.as_view(), name='delete'),
    path('update/<pk>', PostUpdateApiView.as_view(), name='update'),
    path('create', PostCreateApiView.as_view(), name='create'),
]
