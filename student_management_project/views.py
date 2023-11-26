from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import *

def BASE(request):
    return render(request, 'base.html')

# function of views....

def LOGIN(request):
    return render(request, 'login.html')

# function for login user
def dologin(request):
    if request.method == 'POST':
        user= EmailBackend.authenticate(request,
                                          username= request.POST.get('email'),
                                          password= request.POST.get('password'),
                                          )
        if user is not None:
            login(request, user)
            user_type= user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, 'Email and Password are Invalid!!')
                return redirect('login')
        else:
            messages.error(request, 'Email! and Password are Invalid!!')
            return redirect("login")
        

# function for logout user
def dologout(request):
    logout(request)
    return redirect('login')

# function for user profile

def User_Profile(request):
    user= CustomUser.objects.get(id= request.user.id)
    
    context={
        'user': user
    }
    return render(request, 'profile.html', context)
        

def PROFILE_UPDATE(request):
    if request.method == 'POST':
        profile_pic= request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name') 
        # email= request.POST.get('email')
        # username= request.POST.get('username')
        password= request.POST.get('password')
        
        try:
            customuser= CustomUser.objects.get(id= request.user.id)
            
            customuser.first_name= first_name
            customuser.last_name= last_name
            
            if password != None and password != '':
                customuser.set_password(password)
            if profile_pic != None and profile_pic != '':
                customuser.profile_pic= profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('login')
        except:
            messages.error(request, 'Failed to Updated Your Profile Try Again !')
    return render(request, 'profile.html')
        
    
    
def ABOUT_US(request):
    developers_details= About_Us.objects.all()
    
    context= {
        "developers_details": developers_details
    }
    return render(request, 'about_us.html', context)