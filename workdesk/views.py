from django.http import response
from django.shortcuts import render, redirect
from django.http.response import Http404
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.views import LoginView

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from decouple import config
from users.models import User
from django.contrib.auth.models import Group
from .models import Project, List, Member, Card, Comment
from .serializers import GroupSerializer, UserSerializer, ProjectSerializer, ListSerializer, CardSerializer, DetailedCardSerializer, MemberSerializer, CommentSerializer,ShortProjectSerializer, DetailedProjectSerializer
from .permissions import IsProjectMemberOrAdmin, IsListMemberOrAdmin, IsCardMemberOrAdmin, IsAdmin, IsOwnerorReadOnly


class GroupViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for User Group

    Make user either an admin or a normal user
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdmin, IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model User

    Enable or Disable a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin, IsAuthenticated]

    def dispatch(self, *args, **kwargs):
        response = super(UserViewSet, self).dispatch(*args, **kwargs)
        response['Access-Control-Allow-Origin']='http://localhost:3000'
        response['Access-Control-Allow-Credentials']='true'
    
        return response


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model Project

    Create,Delete,Update a project
    """
    queryset = Project.objects.all()
    # serializer_class = ProjectSerializer
    permission_classes = [IsProjectMemberOrAdmin, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DetailedProjectSerializer
        return ProjectSerializer


    def perform_create(self,serializer):
       project_creator=Member.objects.get(users=self.request.user)
       serializer.save(creator = project_creator)

    def dispatch(self, *args, **kwargs):
        response = super(ProjectViewSet, self).dispatch(*args, **kwargs)
        response['Access-Control-Allow-Origin']='http://localhost:3000'
        response['Access-Control-Allow-Credentials']='true'
    
        return response


class ShortProjectViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model Project

    """
    serializer_class = ShortProjectSerializer
    permission_classes = [IsProjectMemberOrAdmin, IsAuthenticated]

    def get_queryset(self):
        project_creator=Member.objects.get(users=self.request.user)
        queryset = (Project.objects.filter(is_public=True)) 
        return queryset


class UserProjectViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for all the projects of current user

    """
    serializer_class = DetailedProjectSerializer
    permission_classes = [IsProjectMemberOrAdmin, IsAuthenticated]

    def get_queryset(self):
        project_member=Member.objects.get(users=self.request.user)
        queryset = (Project.objects.filter(members=project_member))
        return queryset


class ListViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model List

    Create,Delete,Update a list
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsListMemberOrAdmin, IsAuthenticated]

    def dispatch(self, *args, **kwargs):
        response = super(ListViewSet, self).dispatch(*args, **kwargs)
        response['Access-Control-Allow-Origin']='http://localhost:3000'
        response['Access-Control-Allow-Credentials']='true'
    
        return response

class CardViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model Card

    Create,Delete,Update a card
    """
    queryset = Card.objects.all()
    # serializer_class = CardSerializer
    permission_classes = [IsCardMemberOrAdmin, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DetailedCardSerializer
        return CardSerializer

    def perform_create(self,serializer):
       card_creator=Member.objects.get(users=self.request.user)
       serializer.save(creator = card_creator)

    def dispatch(self, *args, **kwargs):
        response = super(CardViewSet, self).dispatch(*args, **kwargs)
        response['Access-Control-Allow-Origin']='http://localhost:3000'
        response['Access-Control-Allow-Credentials']='true'
    
        return response


class UserCardViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for the cards assigned to current user

    """
    serializer_class = CardSerializer
    permission_classes = [IsCardMemberOrAdmin, IsAuthenticated]

    def get_queryset(self):
        card_assignee=Member.objects.get(users=self.request.user)
        queryset = (Card.objects.filter(assignees = card_assignee))
        return queryset


class MemberViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model Members

    Get members data,Update member's admin status
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdmin, IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model Comment

    Create,Update a Comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerorReadOnly, IsAuthenticated]
