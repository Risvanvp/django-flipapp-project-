from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("about page")
def register(request):
       return render(request,'register.html')
    
def login(request):
    return render(request,'login.html')
    
