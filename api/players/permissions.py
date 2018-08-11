from rest_framework import permissions

class IsOwnerPelada(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            True
        return obj.dono == request.user


class IsPelada(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            True
        return obj.pelada.dono == request.user



class PublicEndpoint(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        def has_object_permission(self, request, view, obj):

            if request.method in permissions.SAFE_METHODS:
                return False
            else:
                return obj.dono == request.user