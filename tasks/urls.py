from django.urls import path
from . import views

urlpatterns =[
    path('show-task/',views.show),
    path('show-task/<int:id>/',views.nshow)
    # path('show-task/<int:id>', views.nshow)
]

