from django.shortcuts import render,redirect

# Create your views here.

from django.views import View
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')

class AdminHomeView(View):
        def get(self, request):
            return render(request, 'adminhome.html')
class StudentHomeView(View):
    def get(self,request):
        return render(request,'studenthome.html')

from app1.forms import SignUpForm
class SignUpView(View):

   def get(self,request):
       form_instance=SignUpForm()
       return render(request,'register.html',{'form':form_instance})

   def post(self,request):
       form_instance=SignUpForm(request.POST)
       if form_instance.is_valid():
           form_instance.save()
           return redirect('home')

from app1.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
class SignInView(View):
    def get(self, request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

    def post(self, request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=pwd)
            if user and user.is_superuser==True: #Admin User
                login(request,user)
                return redirect('adminhome')
            elif user and user.is_superuser==False: #Student User
                login(request,user)
                return redirect('studenthome')
            else:
                print("Invalid Credentials")
                return render(request,'login.html')



class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('signin')


from app1.forms import SchoolForm
class AddSchoolView(View):

    def get(self,request):
        form_instance=SchoolForm()
        return render(request,'addschool.html',{'form':form_instance})
    def post(self,request):
        form_instance=SchoolForm(request.POST)

        if form_instance.is_valid():
            form_instance.save()
            return redirect('adminhome')

from app1.models import School

class SchoolListView(View):
    def get(self,request):
        s=School.objects.all()
        return render(request,'schoollist.html',{'schools':s})


class SchoolDetailView(View):
    def get(self,request,i):
        s=School.objects.get(id=i)
        return render(request,'schooldetail.html',{'school':s})
from app1.forms import StudentJoinForm
class StudentJoinView(View):
    def get(self,request,i):
        form_instance=StudentJoinForm()
        return render(request,'studentjoinform.html',{'form':form_instance})

    def post(self,request,i):
        form_instance=StudentJoinForm(request.POST)
        if form_instance.is_valid():
            s=form_instance.save(commit=False)
            s.user=request.user #current logged-in user
            school=School.objects.get(id=i) #School to join
            s.school=school
            s.save()
            return redirect('studenthome')






