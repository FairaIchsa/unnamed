from rest_framework import permissions


class IsNotSelf(permissions.BasePermission):
    message = 'Cannot follow/unfollow yourself'

    def has_object_permission(self, request, view, obj):
        return obj != request.user
