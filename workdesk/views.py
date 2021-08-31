from django.shortcuts import render
from django.http.response import Http404
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from django.views import generic
from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import project,list,member,card


class IndexView(generic.ListView):
    template_name = 'workdesk/index.html'
    def get_queryset(self):
        return 

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = ProjectSerializer 
