from django import forms
from tasks.models import *


# Manual Form Creation (Not model form)
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


""" Mixing to apply style to form field"""
#styledformMixin
class StyleForMixin:
    """ Mixing to apply style to form field"""

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()

    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder':  f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                print("Inside Date")
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                print("Inside checkbox")
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:
                print("Inside else")
                field.widget.attrs.update({
                    'class': self.default_classes
                })



#Django Model Form
class TaskModelForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        fields = ['title','description','due_date','assigned_to']
        widgets={
            'due_date':forms.SelectDateWidget,
            'assigned_to':forms.CheckboxSelectMultiple
        }
        
        # exclude = ['project']
        """Mannual widget """
        # widgets = {
        #     'title' : forms.TextInput(attrs={
        #         'class':"border border-gray-300 w-full rounded-lg shadow-md focus:border-red-800 focus:ring-rose-500",
        #         "placeholder":"Enter Task Title"}),
        #     'description' : forms.Textarea(attrs={
        #         'class':"border border-gray-300 w-full rounded-lg shadow-md focus:border-red-800 focus:ring-rose-500",
        #         "placeholder":"Describe The Task"}),
        #     'due_date' : forms.SelectDateWidget(attrs={
        #         'class':"border border-gray-300  rounded-lg shadow-md focus:border-red-800 focus:ring-rose-500"
        #         }),
        #     'assigned_to' : forms.CheckboxSelectMultiple(attrs={
        #         'class':"space-y-2" # Added spacing between checkboxes for better readability
        #     })
        # }
    '''Using Mixing Widget'''
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs) #Unpack
    #     self.apply_styled_widgets()



class TaskDetailModelForm(StyleForMixin,forms.ModelForm):
    class Meta:
        model = Task_detail
        fields = ["priority","notes","asset"]
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs) #Unpack
    #     self.apply_styled_widgets()








# """ Mixing to apply style to form field"""
# class StyleForMixin:
#     def __init__(self,*args,**kwargs):
#       super().__init__(*args,**kwargs) #Unpack
#       self.apply_styled_widgets()

#     default_classes = "border border-gray-300 w-full rounded-lg shadow-md focus:border-red-800 focus:ring-rose-500"

#     def apply_styled_widgets(self):
#         for field_name, field in self.fields.items():
#             # print(field_name)
#             label = field.label or field_name
#             if isinstance(field.widget,forms.TextInput):
#                 field.widget.attrs.update({
#                     'class':self.default_classes,
#                     'placeholder':f"Enter {field.label.lower()}"
#                 })

#             # elif field.widget.input_type == 'password':
#             elif isinstance(field.widget,forms.PasswordInput):
#              field.widget.attrs.update({ 'class': self.default_classes,  'placeholder': f"Enter {label.lower()}" })

#             elif isinstance(field.widget,forms.Textarea):
#                 field.widget.attrs.update({
#                     'class':self.default_classes,
#                     'placeholder':f"Enter {field.label.lower()}",
#                     'rows':5
#                 })
#             elif isinstance(field.widget,forms.SelectDateWidget):
#                 # print("inside",field_name)
#                 field.widget.attrs.update({
#                     'class':"border border-gray-300 bg-red-300   rounded-lg shadow-md focus:border-red-800 focus:ring-rose-500"
#                 })
#             elif isinstance(field.widget,forms.CheckboxSelectMultiple):
#                 field.widget.attrs.update({
#                     'class':"space-y-2"
#                 })
#             else:
#                 field.widget.attrs.update({ 'class': self.default_classes,  'placeholder': f"Enter {label.lower()}" })
                
