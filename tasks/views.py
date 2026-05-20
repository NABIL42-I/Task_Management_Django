from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm,TaskDetailModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q,Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from users.views import is_admin


def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_employee(user):
    return user.groups.filter(name='Employee').exists()

# def is_admin(user): we import this from users app
#     return user.groups.filter(name='Admin').exists()


# def dashboard(request):
#     return render(request,"Dashboard/dashboard.html")

@login_required
def dashboard(request):
    if is_admin(request.user):
        return redirect('admin_dashboard')
    elif is_manager(request.user):
        print("manager")
        return redirect('manager_dashboard')
    elif is_employee(request.user):
        return redirect('employee_dashboard')
    return redirect('no_permission')





#Read Query ->CRUD
@user_passes_test(is_manager,login_url='no_permission')
def manager_dashboard(request):
    #Getting task count
    # total_tasks = tasks.count()
    # pending = tasks.filter(status="PENDING").count()
    # completed=tasks.filter(status="COMPLETED").count()
    # in_progress=tasks.filter(status="IN_PROGRESS").count()

    # context={
    #     'tasks':tasks,
    #     'total_tasks':total_tasks,
    #     'pending':pending,
    #     'completed':completed,
    #     'in_progress':in_progress
    # }

    type = request.GET.get('type','all')
    # print(type)
    # print(request.GET)
    tasks_base = Task.objects.select_related('New_Details').prefetch_related('assigned_to')

    if type=='completed':
        tasks=tasks_base.filter(status='COMPLETED')
    elif type=='in_progress':
        tasks=tasks_base.filter(status='IN_PROGRESS')
    elif type=='pending':
        tasks=tasks_base.filter(status='PENDING')
    elif type=='all':
        tasks=tasks_base.all()
    
    counts = Task.objects.aggregate(
        total = Count('id'),
        completed = Count('id',filter=Q(status='COMPLETED')),
        in_progress = Count('id',filter=Q(status='IN_PROGRESS')),
        pending = Count('id',filter=Q(status='PENDING'))
    )

    context ={
        'tasks':tasks,
        'counts':counts
    }
    return render(request,"Dashboard/manager_d.html",context)



@user_passes_test(is_employee,login_url='no_permission')
def employee_dashboard(request):
    return render(request,"Dashboard/user_d.html")




#Create Task Form ->CRUD
login_required
@permission_required("tasks.add_task",login_url='no_permission')
def create_task(request):
    # employees = Employee.objects.all()
    # Create object
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)        #FOR PROCECING PICTURE
        task_detail_form = TaskDetailModelForm(request.POST , request.FILES)
        
        #Data  Validate & clean
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False) #obj will create but data will not save in database
            task_detail.task = task
            task_detail.save()
            # return HttpResponse("HI")
            messages.success(request, "Task Created Successfully")
            return redirect('create_task')

    context={"task_form":task_form , "task_detail_form":task_detail_form}
    return render(request,"task_form.html",context)




# update_task = login_required(
#     permission_required("tasks.change_task", login_url='no_permission')(update_task)
# )
#This view has some problem 
#Update Task Form -> CRUD
login_required
@permission_required("tasks.change_task",login_url='no_permission')
def update_task(request,id):
    task=Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)
    #this condition is problemetic
    if task.New_Details : #if task.New_Details exit?
        task_detail_form = TaskDetailModelForm(instance=task.New_Details)
        # try: #try to solve with this
        #    detail = task.New_Details
        # except Task_detail.DoesNotExist:
        #    detail = None
    if request.method == "POST":
        task_form = TaskModelForm(request.POST,instance=task)
        task_detail_form = TaskDetailModelForm(request.POST,instance=task.New_Details)
        #Data  Validate & clean
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail_form = task_detail_form.save(commit=False)
            task_detail_form.task = task
            task_detail_form.save()
            # return HttpResponse("HI")
            messages.success(request, "Task Updated Successfully")
            return redirect('update_task',id)
    context={"task_form":task_form , "task_detail_form":task_detail_form}
    return render(request,"task_form.html",context)




#Delete task form -> CRUD
login_required
@permission_required("tasks.delete_task",login_url='no_permission')
def delete_task(request,id):
    if request.method =="POST":
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request,"One Task has been Deleted")
        return redirect('manager_dashboard')
    else:
        messages.error(request,"Something went wrong")
        return redirect('manager_dashboard')




login_required
@permission_required("tasks.view_task",login_url='no_permission')
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
    # tasks = Task.objects.filter(title__icontains="O",status='IN_PROGRESS')

    '''show the task that contain word 'o' OR  status='IN_Progress'''
    # tasks = Task.objects.filter(Q(title__icontains="O")|Q(status='IN_PROGRESS'))

    # tasks= Task.objects.select_related('New_Details').all()
    # tasks = Project.objects.prefetch_related('task_set').all()   

    # tasks= Task.objects.aggregate(num=Count('title'))

    projects = Project.objects.annotate(
    num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects": projects})


login_required
@permission_required("tasks.view_task",login_url='no_permission')
def task_details(request,task_id):
    task = Task.objects.get(id=task_id)
    status_choices = Task.STATUS_CHOICES
    if request.method =='POST':
        selected_status = request.POST.get('task_status')
        print(selected_status)
        task.status = selected_status
        task.save()
        return redirect('task_details',task_id)
    return render(request,'task_details.html',{'task':task ,'status_choices':status_choices})




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

