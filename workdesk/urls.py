from rest_framework_nested import routers
# from rest_framework import routers
from .views import ShortProjectViewSet, ProjectViewSet, ListViewSet, CardViewSet, MemberViewSet, UserViewSet, GroupViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('user',UserViewSet)
router.register('group',GroupViewSet)
router.register('member',MemberViewSet)
router.register('home',ShortProjectViewSet,basename='projectlist')
router.register('project',ProjectViewSet)
router.register('List',ListViewSet)


list_router = routers.NestedSimpleRouter(router, 'project', lookup='project')
list_router.register('list',ListViewSet,basename='project-list')

card_router = routers.NestedSimpleRouter(router, 'List', lookup='List')
card_router.register('card',CardViewSet,basename='List-card')

# router = routers.DefaultRouter()

# router.register('Project', ProjectViewSet)
# router.register('List', ListViewSet)
# router.register('Card', CardViewSet)
# router.register('Member', MemberViewSet)
# router.register('Comment', CommentViewSet)