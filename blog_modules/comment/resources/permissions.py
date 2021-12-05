from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        """Burası her türlü çalışır ve önceliklidir"""
        return request.user and request.user.is_authenticated

    message = "You must be owner"

    def has_object_permission(self, request, view, obj):
        """burası tetikleme olmadan çalışmaz"""
        return obj.user == request.user
