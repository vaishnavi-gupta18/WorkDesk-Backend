from django.db import models
from django.conf import settings
from django.db.models.fields import DateTimeField
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class project(models.Model):
    title = models.CharField(max_length=100)
    desc = RichTextField()
    start_date = models.DateTimeField(blank=False)
    creator = models.PositiveIntegerField(blank=False)
    status = models.CharField(max_length=100)
    is_pub = models.BooleanField

class member(User):
    projects = models.ManyToManyField(project)
    

class list(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(blank=False)
    project_id = models.ForeignKey(to=project, on_delete=models.CASCADE)
    
class card(models.Model):
    title = models.CharField(max_length=100)
    desc = RichTextField()
    start_date = models.DateTimeField(blank=False)
    due_date = models.DateTimeField(blank=False)
    creator = models.PositiveIntegerField(blank=False)
    assignees = models.ManyToManyField(member)
    list_id = models.ForeignKey(to=list, on_delete=models.CASCADE)


