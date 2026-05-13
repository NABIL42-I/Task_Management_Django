from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=250,label='Task Title')
    description = forms.CharField(widget=forms.Textarea ,label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget ,label="Due Date")
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple , choices = [
    ("x", "Option X"),
    ("y", "Option Y"),
])

    def __init__(self,*args,**kwargs): # args-> tuple, kwargs-> dictionary
        # print(args,kwargs)
        employees = kwargs.pop("employees",[])
        # print("after",employees)
        super().__init__(*args,**kwargs)
        self.fields['assigned_to'].choices=[(emp.id,emp.name) for emp in employees]

