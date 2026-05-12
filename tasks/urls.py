from django.urls import path
from . import views
# from tasks.views import manager

urlpatterns =[
    path("dashboard/",views.dashboard),
    path("manager/",views.manager),
    path("user/",views.user),
    path("test_static/",views.test_static),
    path("test/",views.test),
    path("task_form/",views.task_form)
    
    # path('show-task/',views.show),
    # path('show-task/<int:id>/',views.nshow)
    # # path('show-task/<int:id>', views.nshow)
]

