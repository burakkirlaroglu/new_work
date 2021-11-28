from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from blog_modules.favourite.resources.views import (FavouriteAPIView,
                                                    FavouriteOtherAPIView)

urlpatterns = [
    path('favourite/', FavouriteAPIView.as_view(),
         name='favourite-create-list'),
    path('favourite/<pk>/', FavouriteOtherAPIView.as_view(),
         name='favourite-retrieve-delete')
]
