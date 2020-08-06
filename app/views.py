from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request,'index.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        title=request.POST.get('title')
        message=request.POST.get('message')
        data=Contact(Name=name,Email=email,Title=title,Message=message)
        data.save()
        return HttpResponse("<script>alert('Congratulations ..!! Your query has been succesfully submitted to our team'); window.location.replace('/')</script>")

