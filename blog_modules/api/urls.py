from blog_modules.post.urls import urlpatterns as post_urlpatterns
from blog_modules.comment.urls import urlpatterns as comment_urlpatterns
from blog_modules.favourite.urls import urlpatterns as favourite_urlpatterns

app_name = 'blog'
urlpatterns = [

]

urlpatterns += post_urlpatterns
urlpatterns += comment_urlpatterns
urlpatterns += favourite_urlpatterns
