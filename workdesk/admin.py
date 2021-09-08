from django.contrib import admin
from .models import Project, Member, List, Card
# Register your models here.
admin.site.register(Project)
admin.site.register(Member)
admin.site.register(List)
admin.site.register(Card)
