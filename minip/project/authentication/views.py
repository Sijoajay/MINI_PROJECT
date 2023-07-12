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





config={
  "type": "service_account",
  "project_id": "question-c207f",
  "private_key_id": "c79608ab0f911766f0fb746f8b9f8c08e6f54a3f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDMTkIGUnwFaZsx\n8tk4DgeYgkmbjyzJGh1/KIKd9xS4tZY29xbk+GwGX1GnFXlp+E5j8V4HT8pQIC89\nfIzazfNH0eV+IN674R7lwPpkoDGACnCZjYxvXzkRLSx7V9X02BHufOV9SmBcOv84\nmTGrBmS/p82HnzbW5cinUlmAphsO6d2kEF0cJVRDNPTsGksdlNF6ygIlWmzhxnGH\nRn9EYF4KCOwT4dC6Jryz/OpDVQ2VmPvKc8iaDcXyrBGJvjd+Irdpiw3ingCp7UjX\n6wHefh8mJBNqfw4t50EP9118yVkLwZovulk5YE8VuOQ4/8vrPdIdGOMwQyFXSXV5\nopdW4BrNAgMBAAECggEAX31IQLo2uzTj05Gk0x1DkZV7n9hoX0n0dWVSv1AngDln\nDyOnsLcnjkbo3AYebFghE3dRsmsprQ+N5Ngc4XuW9H93Gt90Gy4aCdqLbZKt8CFx\nBWPyOm+wNYX+n1urZbfDkcsQW+HybckpVqPLYhsn5aghWP0iXYiiownLSWTZirsP\n+wL+ezHCCqc6ahOHrzOU+q14pItgtgatD1xqGUatmrqae/qsJzSZlwyz1z+hYTI2\nJikbMY5gG/Fpbg7pFwz8LRHsKaNObQw7tObg80jYbILChZ76IVlrHqUUQdj3SmeZ\nw2dJmRndLzEDwV9ami23U3uMt7u7dgYDzorsigIBJQKBgQDrpjpHJZ71G8rSOk4Q\nRiQOuXIFScVGr2nylppNW+8a0cS7msuJq/3fPfWSrIJB7YHGFCjol9oPW6mMV2Yz\nwQDlvD8lmDOcx2Xurfn3aa08YeAmz0Z8vuInyjy4wQNuGZwG8+G3B8LukVwoxj+1\nYiqSWf693Q6jwlYJucVP+bWRxwKBgQDd8xSQDGcnf2Ro+Hg660VMzZNMbggfMJHO\n1GDdUucYvCeyWk4L3kGYxfdWnr4QRgStoaOLrwxLIl4ZY4RKqUhFLYJBKyNCMVFy\ntXUiEsidQQRSsu1aLeBp3RlrO/NwriRv5eWUU0zXYKpdrF/tItWswE/O1JWezhzM\n70mO9q5uywKBgGA3bB42rzO3WFYENnGQohJdB8A/Acy9vM2vTmt9uSBDPEe5iZe5\n4Ruwyb9MrpbKqi09eAKYVhHlRFIoMXO6P2qONV5dSd2e0PDmmmS6AmDgOcy+3zH6\nIo9KlQZ+0K64yCtSkvvPsHkGYxHG+KZP4cAF/Ox7AQo+RDEOaBEijU9rAoGBAMF0\nVbD0zpizxi5knE8msGGwMbqFkZi1+fEgVkmzL/D0V1lysuJPWDe0HdEnThzbGsrI\nv8dJzVpT21cf0bhN8ssxTn5E/ld8qzRji3QmkSvX9s+qW42lvRwo9jXsrFTDxMiv\nxrrRHIICJJy/WWFVYo9PlIB/9OXVW28ZBrGQvBufAoGBALmrUKoeUf58UW6lB3Br\neRGcODwYeLPjzS2YY9/19Ds0TeG87mLMGDHvYdW2Ohm6TZnYnyV4/xAIT0b3gqiH\nckAfiDjZAGq3BKjXjjyTuTaO5MRe8fxeLvDOFHms1sG5TIrDbNMsrRrYWzm9NU5A\ngjAuZyErl7KcBtb0a+JjHpQC\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-8hbha@question-c207f.iam.gserviceaccount.com",
  "client_id": "116452727710775218922",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8hbha%40question-c207f.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def home(request):
	day = database.child('Data').child('Day').get().val()
	id = database.child('Data').child('Id').get().val()
	projectname = database.child('Data').child('Projectname').get().val()
	return render(request,"Home.html",{"day":day,"id":id,"projectname":projectname })
