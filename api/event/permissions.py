from rest_framework import permissions


class IsHost(permissions.BasePermission):
    message = 'Only the host can edit events.'

    def has_object_permission(self, request, view, obj):
        return obj.host == request.user


class IsNotHost(permissions.BasePermission):
    message = 'Cannot participate in own events.'

    def has_object_permission(self, request, view, obj):
        return obj.host != request.user
