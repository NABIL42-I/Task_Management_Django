from django.shortcuts import render
from django.http import HttpResponse




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
    return render(request,"task_form.html")

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

