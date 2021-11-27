from blog_modules.post.urls import urlpatterns as post_urlpatterns
from blog_modules.comment.urls import urlpatterns as comment_urlpatterns


app_name = 'post'
urlpatterns = [

]

urlpatterns += post_urlpatterns
urlpatterns += comment_urlpatterns
