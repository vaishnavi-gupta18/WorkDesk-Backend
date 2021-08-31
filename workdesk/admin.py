from django.contrib import admin
from .models import project,member,list,card
# Register your models here.
admin.site.register(project)
admin.site.register(member)
admin.site.register(list)
admin.site.register(card)