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
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from workdesk.urls import router
from workdesk.views import IndexView
from users.views import login_user,afterLogin,logout_user

from decouple import config
urlpatterns = [
    path('admin/', admin.site.urls),
    path('workdesk/',IndexView.as_view(), name='index'),
    path('workdesk/login',login_user, name='login'),
    path('workdesk/logout',logout_user, name='logout'),
    path('workdesk/api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('workdesk/after_login',afterLogin, name='after_login'),
    
]
