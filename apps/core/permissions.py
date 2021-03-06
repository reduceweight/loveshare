from rest_framework import permissions


class IsAdminOrIsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and request.user.is_staff:
            return True
        if request.user.is_authenticated and request.method == 'POST':
            return True
        # Instance must have an attribute named `owner`.
        if getattr(obj, 'owner', False) and obj.owner == request.user:
            return True
        return False