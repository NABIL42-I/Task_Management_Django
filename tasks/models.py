from django.db import models
from django.db.models.signals import post_save,pre_save,m2m_changed,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail

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
        return self.title #tandar Method , it represent object in string representation

    
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
    task = models.OneToOneField(Task, on_delete=models.DO_NOTHING ,related_name="New_Details" )
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

#signal
@receiver(post_save,sender=Task)
def notify_task_creation(sender,instance,created,**kwarges):
    if created:
        print('sender',sender)
        print('instance',instance)
        print(kwarges)
        instance.is_completed = False
        instance.save()

#pre_save
@receiver(pre_save,sender=Task)
def notify_task_creation(sender,instance,**kwarges):
    print('sender',sender)
    print('instance',instance)
    print(kwarges)
    instance.is_completed = True
    # instance.save() wrong (will cause Recursive maximum depth)



# Source - https://stackoverflow.com/a/37529580
# Posted by solarissmoke
# Retrieved 2026-05-17, License - CC BY-SA 3.0

@receiver(m2m_changed, sender=Task.assigned_to.through)
def notify_employees_on_task_creation(sender, instance, action, **kwargs):
    if action == 'post_add':
            assigned_emails= [emp.email for emp in instance.assigned_to.all()]
            send_mail(
                "New Task Assigned",
                f"You have been assigned to the task: {instance.title}",
                "nabilehsanul@gmail.com",
                assigned_emails,
                fail_silently=False
            )


@receiver(post_delete,sender=Task)
def delete_associate_details(sender,instance,**kwarges):
    if instance.New_Details:
        instance.New_Details.delete()
        print("Delete")
