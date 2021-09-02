from rest_framework.permissions import BasePermission
from .models import member

class ProjectWritePermission(BasePermission):
    message = 'Permission denied'
    def has_object_permissions(self,request,view,obj):
        if request.method in SAFE_METHODS or request.user.is_admin:
            return True
        try:
            members = member.objects.filter(projects__id = obj.id)
            print(members)
        except:
            pass

        if request.user in members:
            return True
        return False
        
