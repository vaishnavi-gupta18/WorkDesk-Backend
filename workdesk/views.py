from django.shortcuts import render
from django.http.response import Http404
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from django.views import generic
from rest_framework import viewsets
from .serializers import ProjectSerializer,ListSerializer,CardSerializer,MemberSerializer
from .models import project,list,member,card
from .permissions import ProjectUserWritePermission


class IndexView(generic.ListView):
    template_name = 'workdesk/index.html'
    def get_queryset(self):
        return 

class ProjectViewSet(viewsets.ModelViewSet, ProjectUserWritePermission):
    queryset = project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ProjectUserWritePermission]

class ListViewSet(viewsets.ModelViewSet):
    queryset = list.objects.all()
    serializer_class = ListSerializer 

class CardViewSet(viewsets.ModelViewSet):
    queryset = card.objects.all()
    serializer_class = CardSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = member.objects.all()
    serializer_class = MemberSerializer