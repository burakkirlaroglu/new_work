from rest_framework.generics import CreateAPIView, ListAPIView

from blog_modules.base.permissions import IsOwner
from blog_modules.comment.models import Comment
from blog_modules.comment.resources.serializers import CommentSerializer


class CommentApiViews(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListApiView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
