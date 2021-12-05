from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, \
    RetrieveUpdateAPIView

from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin

from blog_modules.comment.resources.permissions import IsOwner
from blog_modules.comment.models import Comment
from blog_modules.comment.pagination import CommentPagination
from blog_modules.comment.resources.serializers import CommentCreateSerializer, \
    CommandListSerializer, CommandDeleteUpdateSerializer


class CommentCreateApiViews(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListApiView(ListAPIView):
    serializer_class = CommandListSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        """atılan istek çinde q var mı ?
        varsa queryset i filtrele post id'si q'dan sonraki değer ne ise o parent'a
        ait postları dön """
        queryset = Comment.objects.filter(parent=None)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(post=query)
        return queryset


# class CommentDeleteApiView(DestroyAPIView, UpdateModelMixin, RetrieveModelMixin):
#     queryset = Comment.objects.all()
#     serializer_class = CommandDeleteUpdateSerializer
#     permission_classes = [IsOwner]
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class CommentDeleteApiView(DestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommandDeleteUpdateSerializer
#     permission_classes = [IsOwner]


class CommentUpdateApiView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommandDeleteUpdateSerializer
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwars):
        return self.destroy(request, *args, **kwars)
