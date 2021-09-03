# from rest_framework_nested import routers
from rest_framework import routers
from .views import ProjectViewSet,ListViewSet,CardViewSet,MemberViewSet

# router = routers.SimpleRouter()
# router.register('Project',ProjectViewSet)

# list_router = routers.NestedSimpleRouter(router, 'Project', lookup='Project')
# list_router.register('List',ListViewSet)

router = routers.DefaultRouter()

router.register('Project',ProjectViewSet)
router.register('List',ListViewSet)
router.register('Card',CardViewSet)
router.register('Member',MemberViewSet)