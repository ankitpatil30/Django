from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    return render(request,'FIRSTAPPLICATION/signup.html')

def home(request):
    name = "Hello"
    return render(request, 'FIRSTAPPLICATION/home.html')
    # return HttpResponse("Hello, welcome to the Home Page of Nagato Uzumaki")


def about(request):
    return HttpResponse("This is all about Nagato and SixPathsPain")


def contact(request):
    return HttpResponse("contact Nagato here  ")