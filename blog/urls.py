from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [path('admin/', admin.site.urls),
               path('api/post/', include('blog_modules.post.urls', namespace='post')),
               path('api/comment/', include('blog_modules.comment.urls', namespace='comment')),
               path('api/favourite/', include('blog_modules.favourite.urls', namespace='favourite')),
               path('api/user/', include('blog_modules.account.urls', namespace='account')),
               path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
               path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
