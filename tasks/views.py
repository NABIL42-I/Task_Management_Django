from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Task Management System ")
def hi(request):
    return HttpResponse("<h1 style='color : green'>HI , I am here</h1>")
def show(request):
    return HttpResponse("this is task Page")

# Dynamic URL
def nshow(request,id):
    print("Id",id)
    print("Id type",type(id))
    return HttpResponse(f"<h1>New Show {id} type {type(id).__name__} </h1>")
    # return HttpResponse(f"<h1>New Show {id} type {str(type(id))} </h1>")