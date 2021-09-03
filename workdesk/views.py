from django.http import response
from django.shortcuts import render,redirect
from django.http.response import Http404
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from django.views import generic
from django.contrib.auth.views import LoginView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from decouple import config
import requests

from .serializers import ProjectSerializer,ListSerializer,CardSerializer,MemberSerializer
from .models import Project,List,Member,Card
from .permissions import IsTeamMemberOrAdmin,IsAdmin

class IndexView(generic.ListView):
    template_name = 'workdesk/index.html'
    
    def get_queryset(self):
        return 
        

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsTeamMemberOrAdmin]


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer 
    permission_classes = [IsTeamMemberOrAdmin]


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsTeamMemberOrAdmin]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer