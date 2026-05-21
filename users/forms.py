from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User,Permission,Group
import re
from tasks.forms import StyleForMixin
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm


# class RegisterForm(UserCreationForm):
#     class Meta: #can change the behaviour of class
#             model = User
#             fields = ['username','first_name','last_name','password1','password2','email']
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm,self).__init__(*args, **kwargs)
#         # self.fields['username'].help_text=None
#         # self.fields['password1'].help_text=None
#         # self.fields.get('password2').help_text=None
#         '''Field is a dictionary'''
#         # for fieldname,field in self.fields.items():
#         #     field.help_text=""
#         for fieldname in ['username','password1','password2']:
#             self.fields[fieldname].help_text=None
        

############################Sign-up #########################################

''' Customize Form Creation'''
class CustomRegistrationForm(StyleForMixin,forms.ModelForm):
     password1=forms.CharField(widget=forms.PasswordInput)
     confirm_password = forms.CharField(widget=forms.PasswordInput)
     class Meta:
          model = User
          fields = ['username','first_name','last_name','password1','confirm_password','email']
     

    #  '''Using Mixing Widget'''
    #  def __init__(self,*args,**kwargs):
    #   super().__init__(*args,**kwargs) #Unpack
    #   self.apply_styled_widgets()

         



     '''' #Field Error (only check One Field)'''
     def clean_password1(self):
        
        password1 = self.cleaned_data.get('password1')
        errors = []

        if len(password1) < 8:
           errors.append('Password must be at least 8 characters long')

        if not re.search(r'[A-Z]', password1):
           errors.append('Password must contain an uppercase letter')

        if not re.search(r'[a-z]', password1):
            errors.append('Password must contain a lowercase letter')

        if not re.search(r'[0-9]', password1):
            errors.append('Password must contain a number')

        if not re.search(r'[@#$%^&+=]', password1):
            errors.append('Password must contain a special character')

        if errors:
            raise forms.ValidationError(errors)

        return password1
     
        


        #NON-Field Error (Check Two field whether they are similar)
     def clean(self):
       cleaned_data = super().clean()
       password1 = cleaned_data.get("password1") # return dictionary
       confirm_password = cleaned_data.get("confirm_password")

       if password1 and confirm_password and password1 != confirm_password:
        raise forms.ValidationError("Password do not match")
       
       return cleaned_data # return dictionary
     
# clean_password1()  single value ✔
# clean()  full dictionary ✔

# ''' Field Error for Email '''
#you can create such clean_<fieldname> like username , first name etc field
#must be  use def clean_<fieldname>(self)
     def clean_email(self):
        email = self.cleaned_data.get('email') # return dictionary object {key,object}
        email_exist = User.objects.filter(email=email).exists() # check exit or not
        if email_exist:
            raise forms.ValidationError("Email already Exists")
        return email
        
# clean_password1()  single value ✔
# clean()  full dictionary ✔
     
              

     
#########################Login####################################
class loginForm(StyleForMixin, AuthenticationForm):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
   

###########Assigned-role Form###########################
class AssignRoleForm(StyleForMixin,forms.Form):
   role = forms.ModelChoiceField( # To choiceMultiple Field
      queryset=Group.objects.all(),
      empty_label="Select a Role",
   )

class CreateGroupForm(StyleForMixin,forms.ModelForm):
   permissions = forms.ModelMultipleChoiceField(
      queryset=Permission.objects.all(),
      widget=forms.CheckboxSelectMultiple,
      required =False,
      label = 'Assign Permission'
   )

   class Meta:
      model = Group
      fields = ['name','permissions']
   

class CustomChangePasswordForm(StyleForMixin,PasswordChangeForm):
   pass

class CustomPasswordResetForm(StyleForMixin,PasswordResetForm):
   pass

class CustomPasswordResetConfirmForm(StyleForMixin,SetPasswordForm):
   pass

