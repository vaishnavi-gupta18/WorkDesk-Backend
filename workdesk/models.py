from django.db import models
from django.conf import settings
from django.db.models.fields import DateTimeField
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Member(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=False)
    position = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return f"{self.fullname}: {self.position},{self.year}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    start_date = models.DateTimeField(blank=False)
    creator = models.CharField(max_length=12)
    members = models.ManyToManyField(Member)
    status = models.CharField(max_length=100)
    is_public = models.BooleanField
    def __str__(self):
        return f"{self.title}: {self.description},{self.start_date},{self.creator},{self.status},{self.is_public}"

class List(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(blank=False)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}: {self.start_date},{self.project}"
    
class Card(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    start_date = models.DateTimeField(blank=False)
    due_date = models.DateTimeField(blank=False)
    creator = models.CharField(max_length=12)
    assignees = models.ManyToManyField(Member)
    list = models.ForeignKey(to=List, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}: {self.description},{self.start_date},{self.due_date},{self.creator},{self.list}"

