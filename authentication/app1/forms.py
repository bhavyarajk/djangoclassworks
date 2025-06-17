


from django import forms

from django.contrib.auth.models import User


# class SignupForm(forms.ModelForm): #signupform definition
#
#     class Meta:
#         model=User   #already defined inside django.contrib.auth.models
#         fields=['username','password','email','first_name','last_name']



from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']



class LoginForm(forms.Form):

       username=forms.CharField()

       password=forms.CharField()