from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from blog_modules.account.resources.views import (AccountView)

urlpatterns = [
    path('account/me/', AccountView.as_view(), name='account-update'),
]
