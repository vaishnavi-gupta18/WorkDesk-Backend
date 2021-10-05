from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Member


class IsProjectMemberOrAdmin(BasePermission):
    """
    Permissions for project.

    Allows read-only to authenticated users. Restricts delete,update to project members.
    """
    message = 'Permission denied'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user.groups.get(name='admin'):
                return True
        except:
            pass
        if request.user.member in obj.members.all():
            return True
        return False


class IsListMemberOrAdmin(BasePermission):
    """
    Permissions for List.

    Allows read-only to authenticated users. Restricts delete,update to project members to which list belong to.
    """
    message = 'Permission denied'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user.groups.get(name='admin'):
                return True
        except:
            pass
        if request.user.member in obj.project.members.all():
            return True
        return False


class IsCardMemberOrAdmin(BasePermission):
    """
    Permissions for Card.

    Allows read-only to authenticated users. Restricts delete,update to project members to which card belongs to.
    """
    message = 'Permission denied'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user.groups.get(name='admin'):
                return True
        except:
            pass
        if request.user.member in obj.list.project.members.all():
            return True
        return False


class IsAdmin(BasePermission):
    """
    Permissions for Admin users.

    Checks if user is admin user. Admins have greater privileges.
    """
    message = 'Permission denied'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user.groups.get(name='admin'):
                return True
        except:
            pass

        return False


class IsOwnerorReadOnly(BasePermission):
    """
    Permissions for Comments.

    Allows read-only to authenticated users. Restricts delete,update to project members to which card belongs to.
    """
    message = 'Permission denied'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user.groups.get(name='admin'):
                return True
        except:
            pass
        if request.user.member in obj.member.all():
            return True
        return False
