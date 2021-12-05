from django.urls import path
from blog_modules.favourite.resources.views import (FavouriteListCreateAPIView,
                                                    FavouriteAPIView)
app_name='favourite'
urlpatterns = [
    path('list-create', FavouriteListCreateAPIView.as_view(),
         name='create-list'),
    path('update-delete/<pk>', FavouriteAPIView.as_view(),
         name='delete-update')
]
