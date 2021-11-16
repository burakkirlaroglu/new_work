from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     DestroyAPIView, UpdateAPIView,
                                     CreateAPIView, RetrieveUpdateAPIView)
from rest_framework.permissions import (IsAuthenticated, IsAdminUser)
from blog_modules.post.models import Post
from blog_modules.post.resources.serializers import PostSerializer, \
    PostCreateUpdateSerializer
from blog_modules.base.permissions import IsOwner


class PostListViews(ListAPIView):
    #
    # def get_queryset(self):
    #     qs_post = Post.objects.all().filter(is_active=True)
    #     return qs_post
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
    permission_classes = [IsOwner]


class PostDeleteApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
    permission_classes = [IsOwner]


# class PostUpdateApiView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     lookup_field = "slug"
#      """Burada a user'ı b user'ının post'unu güncelleyebilir burada amaç sadece bunun nasıl kullanıldığıdır."""
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)


class PostUpdateApiView(RetrieveUpdateAPIView):
    """RetrieveUpdateApıView ile update ederken var olan dataları görebilirsin
    sadece UpdateAPIView kullanırsan gözükmez"""
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = "slug"
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
