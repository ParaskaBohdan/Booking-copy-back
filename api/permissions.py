from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.method in permissions.SAFE_METHODS and request.user.is_authenticated
    
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated or request.method in permissions.SAFE_METHODS
    
class IsOwnerOrReadOnlyNoAuth(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.method in permissions.SAFE_METHODS