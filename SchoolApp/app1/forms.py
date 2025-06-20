
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
        class Meta:
            model=User
            fields=['username','password1','password2','email']


from app1.models import School,Student

class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields=['name','principal','location']

class StudentJoinForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','age','place']



class LoginForm(forms.Form):
    username = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput)