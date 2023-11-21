from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Contact, Project, About
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    projects=About.objects.all()
    context={"about":projects}
    return render(request,'about.html',context)

def resume(request):
    return render(request,'resume.html')
def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        femail = request.POST.get('email')  # Update this line
        fnumber = request.POST.get('number')
        fdescription = request.POST.get('desc')
        query=Contact(name=fname, email=femail, phonenumber=fnumber,description=fdescription )
        query.save()
        messages.success(request,'Thanks for Contacting Us. We will get back you soon! ')
        return redirect('/contact/')
    return render(request, 'contact.html')   

def projects(request):
    projects=Project.objects.all()
    context={"projects":projects}
    return render(request,'project.html',context)        