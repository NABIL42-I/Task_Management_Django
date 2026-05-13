from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
from tasks.models import *




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
    employees = Employee.objects.all()
    # Create object
    form = TaskForm(employees=employees)
    if request.method == "POST":
        form = TaskForm(request.POST,employees=employees)
        #Data  Validate & clean
        if form.is_valid():
                    # print(form.cleaned_data)
                    data = form.cleaned_data #return dictionary
                    title=data.get('title') #title = data['title']
                    description = data.get('description')
                    due_date = data.get('due_date')
                    assigned_to = data.get('assigned_to')
                    task = Task.objects.create(title=title,description=description,due_date=due_date)
                    #Assign employee to tasks
                    for emp_id in assigned_to:
                         employee = Employee.objects.get(id=emp_id)
                         task.assigned_to.add(employee)

    context={"form":form}
    return render(request,"task_form.html",context)












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

