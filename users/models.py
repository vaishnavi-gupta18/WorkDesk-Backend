from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
class User(AbstractUser):
  username = models.CharField(max_length=12, blank = False, unique = True)
  fullname = models.CharField(max_length=100, blank=False)
  position = models.CharField(max_length=100, blank=False)
  year = models.CharField(max_length=100, blank=False)
  
  REQUIRED_FIELDS = ['fullname', 'year']
  def __str__(self):
      return "{}".format(self.username)