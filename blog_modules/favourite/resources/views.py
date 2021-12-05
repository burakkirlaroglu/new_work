from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from blog_modules.favourite.models import Favourite
from blog_modules.favourite.pagination import FavPagination
from blog_modules.favourite.resources.serializers import \
    FavouriteListCreateSerializer, FavouriteAPISerializer
from blog_modules.favourite.resources.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated


class FavouriteListCreateAPIView(ListCreateAPIView):
    serializer_class = FavouriteListCreateSerializer
    pagination_class = FavPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    pagination_class = FavPagination
    permission_classes = [IsOwner]
