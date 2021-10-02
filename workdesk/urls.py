from rest_framework_nested import routers
# from rest_framework import routers
from .views import ShortProjectViewSet, ProjectViewSet, ListViewSet, CardViewSet, MemberViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('member',MemberViewSet)
router.register('home',ShortProjectViewSet)
router.register('project',ProjectViewSet)

list_router = routers.NestedSimpleRouter(router, 'project', lookup='project')
list_router.register('list',ListViewSet,basename='project-list')

card_router = routers.NestedSimpleRouter(list_router, 'list', lookup='list')
card_router.register('card',CardViewSet,basename='project-list-card')

# router = routers.DefaultRouter()

# router.register('Project', ProjectViewSet)
# router.register('List', ListViewSet)
# router.register('Card', CardViewSet)
# router.register('Member', MemberViewSet)
# router.register('Comment', CommentViewSet)