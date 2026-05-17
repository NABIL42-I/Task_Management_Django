from django.contrib import admin
from .models import Task,Task_detail,Employee,Project

# Register your models here.
admin.site.register(Task)
admin.site.register(Task_detail)
admin.site.register(Employee)
admin.site.register(Project)
