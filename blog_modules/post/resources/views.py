from rest_framework.generics import ListAPIView
from blog_modules.post.models import Post
from blog_modules.post.resources.serializers import PostSerializer


class PostListViews(ListAPIView):

    def get_queryset(self):
        qs_post = Post.objects.all().filter(is_active=True)
        return qs_post

    serializer_class = PostSerializer

