from rest_framework.permissions import BasePermission,SAFE_METHODS
from .models import Member

class IsTeamMemberOrAdmin(BasePermission):
    message = 'Permission denied'
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user.groups.get(name='admins'):
                return True
        except:
            pass
        try:
            if request.user.member in obj.members.all():
                return True
        except:
            pass
        try:
            if request.user.member in obj.project.members.all():
                return True
        except:
            pass
        try:
            if request.user.member in obj.list.project.members.all():
                return True
        except:
            pass
        return False


class IsAdmin(BasePermission):
    message = 'Permission denied'
    def has_permission(self,request,view):
        try:
            if request.method in SAFE_METHODS:
                return True
        except:
            pass
        try:
            if request.user.groups.get(name='admins'):
                return True
        except:
            pass
        return False


class IsOwnerorReadOnly(BasePermission):
    message = 'Permission denied'
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user.member == obj.member:
                return True
        except:
            pass
        return False
