# """api URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from workdesk.urls import router,list_router,card_router
from workdesk.views import ProjectViewSet, ListViewSet, CardViewSet, MemberViewSet, CommentViewSet
from users.views import login_response, login_redirect, logout_user

from decouple import config
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_redirect, name='login'),
    path('logout', logout_user, name='logout'),
    # path('workdesk/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('workdesk/after_login', login_response, name='after_login'),
    path(r'', include(router.urls)),
    path(r'', include(list_router.urls)),
    path(r'', include(card_router.urls)),
    # path('project/<int:project_pk>/', ProjectViewSet.as_view({'get': 'retrieve'}),name='projects'),
    # path('Project/<int:project_pk>/List/<int:list_pk>', ListViewSet.as_view({'get': 'list'}),name='list'),
]
