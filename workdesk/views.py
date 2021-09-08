from django.http import response
from django.shortcuts import render, redirect
from django.http.response import Http404
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.views import LoginView

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from decouple import config
from users.models import User
from .models import Project, List, Member, Card, Comment
from .serializers import UserSerializer, ProjectSerializer, ListSerializer, CardSerializer, MemberSerializer, CommentSerializer
from .permissions import IsProjectMemberOrAdmin, IsListMemberOrAdmin, IsCardMemberOrAdmin, IsAdmin, IsOwnerorReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model User

    Enable or Disable a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin, IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model Project

    Create,Delete,Update a project
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectMemberOrAdmin, IsAuthenticated]


class ListViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model List

    Create,Delete,Update a list
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsListMemberOrAdmin, IsAuthenticated]


class CardViewSet(viewsets.ModelViewSet):
    """
    ModelViewset for model Card

    Create,Delete,Update a card
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsCardMemberOrAdmin, IsAuthenticated]


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
