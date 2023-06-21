from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'authentication/index.html')
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['Email']
        password=request.POST['Password']
        confirm=request.POST['Confirm']

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"Your account has been created")
        return redirect('signin')
    return render(request,"authentication/signup.html")
def signin(request):
     if request.method=="POST":
        username=request.POST['username']
        password=request.POST['Password']

        user=authenticate(username=username ,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Logged In Sucessfully!!")
            return render(request,"authentication/index.html")
            

        else:
            messages.error(request,'Bad Credentials')
            return redirect('home')
     return render(request,"authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')