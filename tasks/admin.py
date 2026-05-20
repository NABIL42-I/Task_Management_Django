from django.contrib import admin
from .models import Task,Task_detail,Project

# Register your models here.
admin.site.register(Task)
admin.site.register(Task_detail)
admin.site.register(Project)
