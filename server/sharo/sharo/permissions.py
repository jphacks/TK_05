from rest_framework import permissions
from rest_framework.exceptions import APIException


class NotAdminException(APIException):
    status_code = 403

class IsStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff:
            raise NotAdminException(detail="You are not admin, I hate you ;P")
        return request.user.is_staff