from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.tokens import default_token_generator
# from .forms import RegisterForm
from users.forms import CustomRegistrationForm,AssignRoleForm,CreateGroupForm
from django.contrib import messages
from users.forms import loginForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Prefetch

#Test for user
def is_admin(user):
    return user.groups.filter(name='Admin').exists()


# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        form = CustomRegistrationForm()
    if request.method =='POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save(commit=False)
            #convert to object and it return this obj to user
            user.is_active = False
            user.set_password(form.cleaned_data.get('password1'))
            print(form.cleaned_data)
            user.save() 
            messages.success(request,"A Confirmation mail Sent. Please check your email")
            return redirect('sign_in')
        else:
            print('form is not valid')
    return render(request,'registration/sign_up.html',{'form':form})


def sign_in(request):
    form = loginForm()
    if request.method=="POST":
        form = loginForm(data=request.POST)
        if form.is_valid():
            print('yesssssssss')
            user = form.get_user()
            if user is not None:
                login(request,user)
                return redirect("home")
            else :
                print("User name none")
        else:
            print("Not valid")

    return render(request,'registration/sign_in.html',{'form':form})


@login_required #Enforce User to Login
def sign_out(request):
    if request.method =="POST":
        logout(request)
        return redirect('sign_in')
    return HttpResponse('<h1>SignOut Page will be Created Soon</h1><h2>Instead You Can Use /core/home For SignOut</h2> <h3>Be Patient & Stay With Us</h3> <b> Thank You For Your Compromise! </b>')
    

def activate_user(request,user_id,token):
    user = User.objects.get(id=user_id)
    try:
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return redirect('sign_in')
        else:
            return HttpResponse('Invalid ID or Token')

    except User.DoesNotExist:
        return HttpResponse('User Not Found')

        


    #########DashBoard for User (Role Based Access Control)

@user_passes_test(is_admin,login_url='no_permission')
def admin_dashboard(request):
    # users = User.objects.all()  #or use this
    users=User.objects.prefetch_related(
        Prefetch('groups',queryset=Group.objects.all(),to_attr='all_groups')
        ).all()
    for user in users:
        # if user.groups.exists(): #Many Query
        if user.all_groups:
            #add new fied user.group_name
            user.group_name = user.all_groups[0].name
        else:
            user.group_name = "No Group Assigned"
    return render(request,'admin/dashboard.html',{'users':users})



@user_passes_test(is_admin,login_url='no_permission')
def assign_role(request,user_id):
    user = User.objects.get(id = user_id)
    form = AssignRoleForm()
    if request.method == 'POST':
        form =AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear() #Remove old roles 
            user.groups.add(role)
            messages.success(request,f"User {user.username} has been assigned to the {role.name}")
            return redirect('admin_dashboard')
    return render(request,'admin/assign_role.html',{'form':form})


@user_passes_test(is_admin,login_url='no_permission')
def create_group(request):
    form = CreateGroupForm()
    if request.method =='POST':
        form = CreateGroupForm(request.POST)

        if form.is_valid():
            group = form.save() # name, permission attributes
            #  permissions = form.cleaned_data.get('permission')
            # group.permissions.set(permissions)
            messages.success(request,f"Group {group.name} has been created successfully")
            return redirect('create_group')
    return render(request,'admin/create_group.html',{'form':form})



@user_passes_test(is_admin,login_url='no_permission')
def group_list(request):
    # groups = Group.objects.all()
    groups = Group.objects.prefetch_related('permissions').all()

    return render(request,'admin/group_list.html',{'groups':groups})















# # sign_in using HTML 
# def sign_in(request):
#     if request.method=="POST":
#         # print(request.POST)#THIS IS A DICTIONARY
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect("home")

#     return render(request,'registration/sign_in.html')


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


