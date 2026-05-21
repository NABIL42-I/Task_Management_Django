from django.urls import path
from . import views
from .views import GreetingView,MorningGreetingView,MorningGreetingView2,CreateTask,ViewProject,TaskDetail,UpdateTask
# from tasks.views import manager

urlpatterns =[
    path("dashboard/",views.dashboard,name="dashboard"),
    path("manager_dashboard/",views.manager_dashboard,name="manager_dashboard"),
    path("employee_dashboard/",views.employee_dashboard,name='employee_dashboard'),
    path("create_task/",CreateTask.as_view(),name='create_task'),#Class-based-View
    # path("create_task/",views.create_task,name='create_task'),
    # path("view_project/",views.view_project,name="view_project"),
    path("view_project/",ViewProject.as_view(),name="view_project"),#'class-view
    # path("task_details/<int:task_id>",views.task_details,name="task_details"),
    path("task_details/<int:task_id>",TaskDetail.as_view(),name="task_details"),
    # path("update_task/<int:id>/",views.update_task,name="update_task"),
    path("update_task/<int:id>/",UpdateTask.as_view(),name="update_task"),
    path("delete_task/<int:id>/",views.delete_task,name="delete_task"),
    path("greetings/",MorningGreetingView2.as_view(),name='greetings'),
    path("as_view/",MorningGreetingView2.as_view(greeting="This is from the as_view"),name='greetings'),    
]
    #Dynamic 
    # path('show-task/',views.show),
    # path('show-task/<int:id>/',views.nshow)
    # # path('show-task/<int:id>', views.nshow)
