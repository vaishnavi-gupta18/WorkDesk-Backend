from rest_framework import serializers
from users.models import User
from .models import Project,List,Member,Card
class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
      model = Project
      fields = "__all__"

class ListSerializer(serializers.ModelSerializer):
  class Meta:
      model = List
      fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
  class Meta:
      model = Member
      fields = "__all__"

class CardSerializer(serializers.ModelSerializer):
  class Meta:
      model = Card
      fields = "__all__"