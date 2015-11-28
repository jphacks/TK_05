from rest_framework import permissions
from rest_framework.exceptions import APIException, AuthenticationFailed

class IsStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff:
            raise AuthenticationFailed(detail="You are not admin, I hate you ;P")
        return request.user.is_staff