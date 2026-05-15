from django.urls import path
from . import views
# from tasks.views import manager

urlpatterns =[
    path("dashboard/",views.dashboard,),
    path("manager/",views.manager,name="manager"),
    path("user/",views.user),
    path("test_static/",views.test_static),
    path("test/",views.test),
    path("task_form/",views.task_form,name='create_task'),
    path("view_task/",views.view_task),
    path("update_task/<int:id>/",views.update_task,name="update_task"),
    path("delete_task/<int:id>/",views.delete_task,name="delete_task")
    

]
    #Dynamic 
    # path('show-task/',views.show),
    # path('show-task/<int:id>/',views.nshow)
    # # path('show-task/<int:id>', views.nshow)
