from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     DestroyAPIView, UpdateAPIView,
                                     CreateAPIView, RetrieveUpdateAPIView)

from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import (IsAuthenticated, IsAdminUser)
from rest_framework.filters import SearchFilter, OrderingFilter
from blog_modules.post.models import Post
from blog_modules.post.pagination import PostPagination
from blog_modules.post.resources.serializers import PostSerializer, \
    PostCreateUpdateSerializer
from blog_modules.base.permissions import IsOwner


class PostListViews(ListAPIView, CreateModelMixin):
    #
    # def get_queryset(self):
    #     qs_post = Post.objects.filter(is_active=True)
    #     return qs_post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    """Filtreleme için kullanılır, filter tipleri mevcuttur. Uygun olan seçip
    kullanılabilir."""
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']

    pagination_class = PostPagination
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"
    permission_classes = [IsOwner, IsAuthenticated]


class PostDeleteApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"
    permission_classes = [IsOwner, IsAuthenticated]


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
    lookup_field = "pk"
    permission_classes = [IsOwner, IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostCreateApiView(CreateAPIView, ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


