from django.db.models.signals import post_save,pre_save,m2m_changed,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from tasks.models import Task


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
