"""
URL configuration for Task_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings
from tasks import views
from core.views import home
# from tasks.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/",include("tasks.urls")),
    path("users/",include("users.urls")),
    path("core/",include("core.urls")),
    path("home/",home,name="home")
    # path("dashboard/",views.dashboard,name="dashboard"),
]+ debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)