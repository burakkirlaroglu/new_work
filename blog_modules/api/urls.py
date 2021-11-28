from blog_modules.post.urls import urlpatterns as post_urlpatterns
from blog_modules.comment.urls import urlpatterns as comment_urlpatterns
from blog_modules.favourite.urls import urlpatterns as favourite_urlpatterns
from rest_framework_simplejwt import views as jwt_views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='refresh-token'),
]

urlpatterns += post_urlpatterns
urlpatterns += comment_urlpatterns
urlpatterns += favourite_urlpatterns
