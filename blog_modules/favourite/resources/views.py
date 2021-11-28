from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog_modules.favourite.models import Favourite
from blog_modules.favourite.pagination import FavPagination
from blog_modules.favourite.resources.serializers import FavouriteSerializer, \
    FavouriteOtherSerializer


class FavouriteAPIView(ListCreateAPIView):
    #queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    pagination_class = FavPagination

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavouriteOtherAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteOtherSerializer
    pagination_class = FavPagination

