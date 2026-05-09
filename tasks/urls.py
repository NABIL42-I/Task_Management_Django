from django.urls import path
from . import views

urlpatterns =[
    path('show-task/',views.show)
]

