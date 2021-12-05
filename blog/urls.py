from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('api/v1/blog/', include('blog_modules.api.urls', namespace='blog')),
                  path('api/v1/post/',
                       include('blog_modules.post.urls', namespace='post')),
                  path('api/v1/comment/', include('blog_modules.comment.urls',
                                                 namespace='comment')),
                  path('api/v1/favourite/',
                       include('blog_modules.favourite.urls',
                               namespace='favourite'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
