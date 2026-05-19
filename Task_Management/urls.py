"""
URL configuration for Task_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

# from tasks.views import home
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/",include("tasks.urls")),
    path("users/",include("users.urls")),
    path("core/",include("core.urls"))
]+ debug_toolbar_urls()
