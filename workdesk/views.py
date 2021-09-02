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
from .serializers import ProjectSerializer,ListSerializer,CardSerializer,MemberSerializer
from .models import project,list,member,card
from decouple import config
from rest_framework.response import Response
import requests

class IndexView(generic.ListView):
    template_name = 'workdesk/index.html'
    
    def get_queryset(self):
        return 

def Login(request):  
    return redirect('{}client_id={}&redirect_uri={}'.format(config("SITE"),config("CLIENT_ID"),config("REDIRECT_URI")))

def AfterLogin(request):
    response = request.GET
    code = response["code"]
    post_data = {'client_id': '{}'.format(config("CLIENT_ID")),
    'client_secret': '{}'.format(config("CLIENT_SECRET")),
    'grant_type': 'authorization_code',
    'redirect_uri': '{}'.format(config("REDIRECT_URI")),
    'code': '{}'.format(code)
    }
    print(post_data)
    # r = requests.post('{}'.format(config("CODE_SITE")), data=post_data)
    # print(r.json())
    return render(request, 'workdesk/login.html')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = ProjectSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = list.objects.all()
    serializer_class = ListSerializer 

class CardViewSet(viewsets.ModelViewSet):
    queryset = card.objects.all()
    serializer_class = CardSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = member.objects.all()
    serializer_class = MemberSerializer