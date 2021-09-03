from rest_framework import routers
from .views import ProjectViewSet,ListViewSet,CardViewSet,MemberViewSet

router = routers.DefaultRouter()
router.register('Project',ProjectViewSet)
router.register('List',ListViewSet)
router.register('Card',CardViewSet)
router.register('Member',MemberViewSet)