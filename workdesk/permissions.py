from rest_framework.permissions import BasePermission
from .models import member
class ProjectUserWritePermission(BasePermission):
    message = 'Editing projects is restricted to project members only.'

    def has_object_permissions(self,request,view, obj):
        if request.method in SAFE_METHODS:
            return True

        try:
            members = member.objects.filter(projects__id = obj.id)
            print(members)
        except:
            pass

        if request.user in members:
            return
        
