from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
import pyrebase
# Create your views here.
def home(request):
    return render(request,'authentication/index.html')
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['Email']
        password=request.POST['Password']
        confirm=request.POST['Confirm']

        # myuser=User.objects.create_user(username,email,password)
        # myuser.save()
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
            #return render(request,"authentication/deptt.html")
            return redirect('updatecontent')
            

        else:
            messages.error(request,'Bad Credentials')
            return redirect('home')
     return render(request,"authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
def update_content(request):
    if request.method == 'POST':
        selected_checkboxes = request.POST.getlist('checkbox', [])
        dropdown1 = request.POST.get('dropdown1', '')
        dropdown2 = request.POST.get('dropdown2', '')
        
        if len(selected_checkboxes) == 1 and dropdown1 and dropdown2:
            selected_checkbox = selected_checkboxes[0]
            # Determine the new content based on selected options
            
            # Redirect to another HTML page passing the selected options as query parameters
            return redirect(f'dashboard/?checkbox={selected_checkbox}&dropdown1={dropdown1}&dropdown2={dropdown2}')
    return render(request, 'authentication/deptt.html')
def dashboard(request):
    # Get the query parameters from the URL
    checkbox = request.GET.get('checkbox', '')
    dropdown1 = request.GET.get('dropdown1', '')
    dropdown2 = request.GET.get('dropdown2', '')

    # Determine the new content based on selected options

    context = {
        'checkbox': checkbox,
        'dropdown1': dropdown1,
        'dropdown2': dropdown2,
    }

    return render(request,'authentication/dashboard.html')
# from django.shortcuts import render
# import pyrebase
# config
# "piKey": "AIzasyDQqNOoPwWSmYnMYOSRBVFSCII_-7CMWMO"
# "authDomain": "test-a6917.firebaseapp.com",
# "databaseURL": "https://test-a6917-default-rtdb.firebaseio.com"
# "projectId": "test-a6917",
# "storageBucket": "test-a6917.appspot.com",
# "messagingSenderId": "710089216382",
# "appId": "1:710089216382:web:559414a79cbb4aa9f232f"
# def index(request) :
# return render (request, 'index.htm1*) 





config= {
    "apiKey": "AIzaSyCqZ_M4qZKimJS3OJtFYw4vYeohnSY7jG0",
    "authDomain": "question-c207f.firebaseapp.com",
    "projectId": "question-c207f",
    "databaseURL": "https://question-c207f-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket": "question-c207f.appspot.com",
    "messagingSenderId": "147631869987",
    "appId": "1:147631869987:web:08fcd8d93704d2b7766196"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def trial(request):
	day = database.child('Data').child('Day').get().val()
	id = database.child('Data').child('Id').get().val()
	projectname = database.child('Data').child('Projectname').get().val()
	return render(request,"authentication/trial.html",{"day":day,"id":id,"projectname":projectname })
