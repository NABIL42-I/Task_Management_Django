from django.urls import path
from . import views
# from tasks.views import manager

urlpatterns =[
    path("dashboard/",views.dashboard),
    path("manager_dashboard/",views.manager_dashboard,name="manager_dashboard"),
    path("employee_dashboard/",views.employee_dashboard,name='employee_dashboard'),
    path("create_task/",views.create_task,name='create_task'),
    path("view_task/",views.view_task),
    path("task_details/<int:task_id>",views.task_details,name="task_details"),
    path("update_task/<int:id>/",views.update_task,name="update_task"),
    path("delete_task/<int:id>/",views.delete_task,name="delete_task")
    

]
    #Dynamic 
    # path('show-task/',views.show),
    # path('show-task/<int:id>/',views.nshow)
    # # path('show-task/<int:id>', views.nshow)
