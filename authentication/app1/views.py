from django.shortcuts import render,redirect

#Class Based using View class

from django.views import View
from app1.forms import SignupForm

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')

#Register View
class SignupView(View):

    def post(self,request): #After Form submission
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            # user=form_instance.save(commit=False) #here user represents model_instance created
            # # user.set_password(raw_data)
            # user.set_password(form_instance.cleaned_data['password']) #changes the plaintext password
            #                                        #format into encrypted format using django's
            #                                        #SHA algorithm.So here we call built-in function
            #                                        #set_password().
            # user.save()


            form_instance.save()

            return redirect('home')

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
            if user:
                #starting session using current user
                login(request,user)
                # u=request.user
                # print(u)
                # print(u.username)
                # print(u.email)
                # print(u.first_name)
                return redirect('home')
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









