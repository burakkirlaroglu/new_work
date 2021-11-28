from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, \
    RetrieveUpdateAPIView

from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin

from blog_modules.base.permissions import IsOwner
from blog_modules.comment.models import Comment
from blog_modules.comment.pagination import CommentPagination
from blog_modules.comment.resources.serializers import CommentSerializer, \
    CommandChildSerializer


class CommentApiViews(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListApiView(ListAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommandChildSerializer
    pagination_class = CommentPagination

    # def get_queryset(self):
    #     return Comment.objects.filter(parent=None)

    def get_queryset(self):
        """atılan istek çinde q var mı ?
        varsa queryset i filtrele post id'si q'dan sonraki değer ne ise o parent'a
        ait postları dön """
        queryset = Comment.objects.filter(parent=None)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(post=query)
        return queryset


# class CommentDestroyApiView(DestroyAPIView, UpdateModelMixin, RetrieveModelMixin):
#     queryset = Comment.objects.all()
#     serializer_class = CommandChildSerializer
#     permission_classes = [IsOwner]
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class CommentDestroyApiView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommandChildSerializer
    permission_classes = [IsOwner]


class CommentUpdateApiView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommandChildSerializer
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
