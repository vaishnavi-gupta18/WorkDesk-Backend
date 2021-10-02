from django.db import models
from django.conf import settings
from django.db.models.fields import DateTimeField
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField

User = get_user_model()


class Member(models.Model):
    """
    Member details.

    Personal and projects details of users.
    """
    users = models.OneToOneField(User, related_name='member', on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=False)
    position = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.fullname}: {self.position},{self.year}"


class Project(models.Model):
    """
    Project details.

    Details of projects.
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    start_date = models.DateTimeField(blank=False)
    creator = models.ForeignKey(to=Member,primary_key = False,on_delete=models.SET_NULL, null=True,related_name = 'project_creator')
    members = models.ManyToManyField(Member)
    status = models.CharField(max_length=100)
    is_public = models.BooleanField()

    def __str__(self):
        return f"{self.title}: {self.description},{self.start_date},{self.creator},{self.status},{self.is_public}"


class List(models.Model):
    """
    List details.

    Details of lists present the project.
    """
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(blank=False)
    project = models.ForeignKey(to=Project, related_name='lists', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: {self.start_date},{self.project}"


class Card(models.Model):
    """
    Card details.

    Details of cards in a list present in the project.
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    start_date = models.DateTimeField(blank=False)
    due_date = models.DateTimeField(blank=False)
    creator = models.ForeignKey(to=Member,primary_key = False,on_delete=models.SET_NULL, null=True,related_name = 'card_creator')
    assignees = models.ManyToManyField(Member)
    list = models.ForeignKey(to=List, related_name='cards', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: {self.description}, {self.start_date}, {self.due_date}, {self.creator}, {self.list}"


class Comment(models.Model):
    """
    Comment details.

    Details of comments posted by users on card.
    """
    member = models.ForeignKey(to=Member, related_name='comments', on_delete=models.CASCADE)
    card = models.ForeignKey(to=Card, related_name='comments_card', on_delete=models.CASCADE)
    date_created = models.DateTimeField(blank=False)
    body = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.member},{self.card},{self.date_created},{self.body}"
