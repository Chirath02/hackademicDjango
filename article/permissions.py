from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "Must be owner of this post to update it."

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
