from rest_framework import serializers
from django.contrib.auth.models import Group

from users.models import User
from .models import Project, List, Member, Card, Comment


class GroupSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for User Group
    """
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for User model
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'groups', 'is_active']


class MemberSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Member model
    """
    class Meta:
        model = Member
        fields = ['id', 'users', 'fullname', 'position', 'year','email_address','display_picture']


class CommentSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Comment model
    """
    class Meta:
        model = Comment
        fields = ['id', 'member', 'card', 'date_created', 'body']


class DetailedCommentSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Comment model
    """
    member = MemberSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'member', 'card', 'date_created', 'body']


class CardSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Card model
    """
    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'start_date', 'due_date', 'creator', 'assignees', 'list']


class ShortListSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for List model 
    """
    class Meta:
        model = List
        fields = ['id', 'title']


class DetailedCardSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Card model with assignees details
    """
    comments_card= DetailedCommentSerializer(many=True, read_only=True)
    assignees = MemberSerializer(many=True, read_only=True)
    list = ShortListSerializer(read_only=True)
    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'start_date', 'due_date', 'creator', 'assignees', 'list', 'comments_card']


class ListSerializer(serializers.ModelSerializer):
    """
    Nested ModelSerializer for List model including cards
    """
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ['id', 'title', 'start_date', 'project', 'cards']


class ProjectSerializer(serializers.ModelSerializer):
    """
    Nested ModelSerializer for Project model including lists,cards
    """
    lists = ListSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'start_date', 'creator', 'members', 'status', 'is_public', 'lists']


class DetailedProjectSerializer(serializers.ModelSerializer):
    """
    Nested ModelSerializer for Project model including lists,cards
    """
    lists = ListSerializer(many=True, read_only=True)
    members = MemberSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'start_date', 'creator', 'members', 'status', 'is_public', 'lists']


class ShortProjectSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Project model 
    """
    members = MemberSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'start_date', 'creator', 'members', 'status', 'is_public']
