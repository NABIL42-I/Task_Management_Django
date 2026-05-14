from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q,Count



def dashboard(request):
    return render(request,"Dashboard/dashboard.html")

def manager(request):
    return render(request,"Dashboard/manager_d.html")

def user(request):
    return render(request,"Dashboard/user_d.html")

def test_static(request):
    return render(request,"Dashboard/test_static.html")

def test(request):
    print("Hello this  is work in back-end")
    context={
        "Name":["Hello","I","am","here"],
        "age" :["Age","doesn't","matter"],
        "front":["Hello this is in front-end"]
    }
    return render(request,"test.html",context)


def task_form(request):
    # employees = Employee.objects.all()
    # Create object
    form = TaskModelForm()
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        #Data  Validate & clean
        if form.is_valid():
            form.save()
            # return HttpResponse("HI")
            return render(request,"task_form.html",{"form":form , "massage":"Task Added Succesfully"})

    context={"form":form}
    return render(request,"task_form.html",context)


def view_task(request):
    #retrive all data from tasks model
    tasks = Task.objects.all()
    #retrive a specific task
    # task1 = Task.objects.get(pk=1)#pk = primary key or use id
    # task1 = Task.objects.first()#fetch first task
    # tasks = Task.objects.filter(status="PENDING") #FILTER
    
    #show the task which due_date is today
    # tasks=Task.objects.filter(due_date=date.today())

    #show the task whoose priority is not low
    # tasks = Task_detail.objects.exclude(priority='L')

    '''show the task that contain word 'o' and  status='IN_Progress'''
    tasks = Task.objects.filter(title__icontains="O",status='IN_PROGRESS')

    '''show the task that contain word 'o' OR  status='IN_Progress'''
    # tasks = Task.objects.filter(Q(title__icontains="O")|Q(status='IN_PROGRESS'))

    # tasks= Task.objects.select_related('New_Details').all()
    # tasks = Project.objects.prefetch_related('task_set').all()   

    tasks= Task.objects.aggregate(num=Count('title'))
    return render(request,"show_task.html",{"tasks":tasks,"hi":5})




# FORM MANUALLY

# def task_form(request):
#     employees = Employee.objects.all()
#     # Create object
#     form = TaskModelForm()
#     if request.method == "POST":
#         form = TaskModelForm(request.POST)
#         #Data  Validate & clean
#         if form.is_valid():
#                     """For ModelForm Data"""
#                     form.save()
#                     '''For Django Form Data'''
#                     # # print(form.cleaned_data)
#                     # data = form.cleaned_data #return dictionary
#                     # title=data.get('title') #title = data['title']
#                     # description = data.get('description')
#                     # due_date = data.get('due_date')
#                     # assigned_to = data.get('assigned_to')
#                     # task = Task.objects.create(title=title,description=description,due_date=due_date)
#                     # #Assign employee to tasks
#                     # for emp_id in assigned_to:
#                     #      employee = Employee.objects.get(id=emp_id)
#                     #      task.assigned_to.add(employee)
#                     return HttpResponse("Task ADD")

#     context={"form":form}
#     return render(request,"task_form.html",context)





# Create your views here.
# def home(request):
#     return render(request,"home.html")
# def hi(request):
#     return HttpResponse("<h1 style='color : green'>HI , I am here</h1>")
# def show(request):
#     return HttpResponse("this is task Page")
# # Dynamic URL
# def nshow(request,id):
#     print("Id",id)
#     print("Id type",type(id))
#     return HttpResponse(f"<h1>New Show {id} type {type(id).__name__} </h1>")
#     # return HttpResponse(f"<h1>New Show {id} type {str(type(id))} </h1>")

