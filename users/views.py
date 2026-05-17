from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# from .forms import RegisterForm
from .forms import CustomRegistrationForm


# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        form = CustomRegistrationForm()
    if request.method =='POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save() #to save to database
            # # print(form.cleaned_data)
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # confirm_pass = form.cleaned_data.get('password2')
            # if password == confirm_pass:
            #     user = User.objects.create_user(username=username,password=password)
            #     # form.save() #to save to database
            # else:
            #     print('Password do not same')
        else:
            print('form is not valid')

    return render(request,'registration/sign_up.html',{'form':form})

def sign_in(request):
    if request.method=="POST":
        # print(request.POST)#THIS IS A DICTIONARY
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")

    return render(request,'registration/sign_in.html')

def sign_out(request):
    if request.method =="POST":
        logout(request)
        return redirect('sign_in')





# # Create your views here ( RegisterForm)
# def sign_up(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#     if request.method =='POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save() #to save to database
#             # # print(form.cleaned_data)
#             # username = form.cleaned_data.get('username')
#             # password = form.cleaned_data.get('password')
#             # confirm_pass = form.cleaned_data.get('password2')
#             # if password == confirm_pass:
#             #     user = User.objects.create_user(username=username,password=password)
#             #     # form.save() #to save to database
#             # else:
#             #     print('Password do not same')
#         else:
#             print('form is not valid')

#     return render(request,'registration/sign_up.html',{'form':form})


