from django.db import models

# Create your models here.

#one project can have many task
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ("IN_PROGRESS",'In Progress'),
        ('COMPLETED','Completed')
    ]

    #Many to One ## this project name or field name will use for query or reverse or forward relation
    project=models.ForeignKey("Project",on_delete=models.CASCADE ,default=1)

    #Many to Many
    assigned_to=models.ManyToManyField(Employee)

    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField(default="2026-05-13")
    status=models.CharField(max_length=15,choices= STATUS_CHOICES,default="PENDING")
    is_completed= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title #tandar Method

    
#One to One 

# One task only have one task_detail
class Task_detail(models.Model):
    HIGH = 'H'
    MEDIUM ='M'
    LOW ='L'
    PRIORITY_OPTIONS = (
        (HIGH,"HIGH"),
        (MEDIUM,"MEDIUM"),
        (LOW,"LOW")
    )
    #taskdetail_set ->autometically create after build OneToOne rlt
    task = models.OneToOneField(Task, on_delete=models.CASCADE ,related_name="New_Details" )
    # assigned_to = models.CharField(max_length=100)                       #reverse relation
    priority = models.CharField(max_length=1,choices= PRIORITY_OPTIONS,default="L")
    notes = models.TextField(blank=True,null=True)
    def __str__(self):
        return f"Details form Task{self.task.title}"
    
    
#Many to one
#one project can have many task
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    start_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


