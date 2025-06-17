from django.shortcuts import render,redirect

#Class Based using View class

from django.views import View
from app1.forms import SignupForm


from django.contrib import messages
class IndexView(View):
    def get(self,request):
        return render(request,'home.html')

from django.core.mail import send_mail
#

class StudentHomeView(View):
    def get(self,request):
        return render(request,'studenthome.html')

class TeacherHomeView(View):
    def get(self,request):
        return render(request,'teacherhome.html')

class AdminHomeView(View):
    def get(self,request):
        return render(request,'adminhome.html')

#Register View
class SignupView(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():


            user=form_instance.save(commit=False)
            user.is_active=False #After otp verification it will set to True.
            user.save()
            user.generate_otp()
            send_mail(
                "Django Auth OTP",
                user.otp,
                "bhavyaluminar@gmail.com",
                [user.email],
                fail_silently=False,
            )


            return redirect('verify')

    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})

from app1.forms import LoginForm
from django.contrib.auth import authenticate,login

class SigninView(View):

    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # print(name,pwd)
            user=authenticate(username=name,password=pwd)
            #authenticate() returns user object if all the user credentials are correct else none
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('ahome')
            elif user and user.role=="student":
                login(request, user)
                return redirect('shome')
            elif user and user.role=="teacher":
                login(request, user)
                return redirect('thome')

            else:
                print("invalid user credentials")
                return redirect('signin')

    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})



from django.contrib.auth import logout

class SignOutView(View):
    def get(self,request):
        logout(request)       #Removes the user from current session
        return redirect('signin')


from app1.models import CustomUser
class OtpVerificationView(View):

    def post(self,request):
        otp=request.POST.get('otp')
        print(otp)
        try:
            u=CustomUser.objects.get(otp=otp)
            u.is_active=True
            u.is_verified=True
            u.otp=None
            u.save()
            return redirect('signin')
        except:
            # print("invalid otp")
            messages.error(request,"Invalid OTP")
            return redirect('verify')
    def get(self,request):
        return render(request,'otp_verify.html')












