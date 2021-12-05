from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from blog_modules.account.models import Account
from blog_modules.account.resources.serializers import UserSerializer


class AccountView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = Account.objects.all()

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
