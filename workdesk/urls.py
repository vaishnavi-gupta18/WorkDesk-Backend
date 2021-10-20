from rest_framework_nested import routers
from django.urls import path
from .views import ShortProjectViewSet, ProjectViewSet, UserProjectViewSet, UserCardViewSet, ListViewSet, CardViewSet, MemberViewSet, UserViewSet, GroupViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('user',UserViewSet)
router.register('group',GroupViewSet)
router.register('member',MemberViewSet)
router.register('home',ShortProjectViewSet,basename='projectlist')
router.register('project',ProjectViewSet)
router.register('userproject',UserProjectViewSet,basename='userproject')
router.register('usercard',UserCardViewSet,basename='usercard')
router.register('List',ListViewSet)
router.register('Card',CardViewSet)


list_router = routers.NestedSimpleRouter(router, 'project', lookup='project')
list_router.register('list',ListViewSet,basename='project-list')

card_router = routers.NestedSimpleRouter(router, 'List', lookup='List')
card_router.register('card',CardViewSet,basename='List-card')

