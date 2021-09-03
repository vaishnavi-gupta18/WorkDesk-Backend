from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from users.models import User
from .models import Project,List,Member,Card


class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['id','username','groups']


class MemberSerializer(serializers.ModelSerializer):
  class Meta:
      model = Member
      fields = ['id','users','fullname','position','year']
      

class CardSerializer(serializers.ModelSerializer):
  class Meta:
      model = Card
      fields = ['id','title','description','start_date','due_date','creator','assignees','list']


class ListSerializer(serializers.ModelSerializer):
  cards = CardSerializer(many=True)
  
  class Meta:
      model = List
      fields = ['id','title','start_date','project','cards']


class ProjectSerializer(serializers.ModelSerializer):
  lists = ListSerializer(many=True)

  class Meta:
      model = Project
      fields = ['id','title','description','start_date','creator','members','status','is_public','lists']
