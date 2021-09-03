from rest_framework.permissions import BasePermission
from .models import Member

class ProjectWritePermission(BasePermission):
    message = 'Permission denied'
    def has_object_permissions(self,request,view,obj):
        if request.method in SAFE_METHODS or request.user.is_admin:
            return True
        try:
            Members = Member.objects.filter(Projects__id = obj.id)
            print(Members)
        except:
            pass

        if request.user in Members:
            return True
        return False
        
