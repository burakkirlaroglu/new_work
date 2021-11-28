from rest_framework.pagination import PageNumberPagination


class FavPagination(PageNumberPagination):
    page_size = 2
