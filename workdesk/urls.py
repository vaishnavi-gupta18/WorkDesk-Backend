from rest_framework import routers
from .views import ProjectViewSet,ListViewSet,CardViewSet,MemberViewSet

router = routers.DefaultRouter()
router.register('project',ProjectViewSet)
router.register('list',ListViewSet)
router.register('card',CardViewSet)
router.register('member',MemberViewSet)