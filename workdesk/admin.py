from django.contrib import admin

from .models import Project, Member, List, Card, Comment

admin.site.register(Project)
admin.site.register(Member)
admin.site.register(List)
admin.site.register(Card)
admin.site.register(Comment)
