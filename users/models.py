from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
class User(AbstractUser):
  username = models.CharField(max_length=12, blank = False, unique = True)
  def __str__(self):
        return f"{self.username}: {self.fullname}"