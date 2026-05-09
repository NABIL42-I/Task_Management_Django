from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Task Management System")
def hi(request):
    return HttpResponse("<h1 style='color : green'>HI , I am here</h1>")
def show(request):
    return HttpResponse("this is task Page")