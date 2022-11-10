from django.contrib import admin
from .models import Task

# django admin panelinde Task modelinin gorunmesini sagliyor
admin.site.register(Task)
