from rest_framework import serializers
from users.models import User
from .models import project,list,member,card
class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
      model = project
      fields = "__all__"

class ListSerializer(serializers.ModelSerializer):
  class Meta:
      model = list
      fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
  class Meta:
      model = member
      fields = "__all__"

class CardSerializer(serializers.ModelSerializer):
  class Meta:
      model = card
      fields = "__all__"