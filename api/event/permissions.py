from rest_framework import permissions


class IsHostOrReadOnly(permissions.BasePermission):
    message = 'Only the host can edit events.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.host == request.user
