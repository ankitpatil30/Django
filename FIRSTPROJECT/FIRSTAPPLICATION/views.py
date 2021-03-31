from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def signup(request):
    return render(request,'FIRSTAPPLICATION/signup.html')

def portfolio(request):
    return render(request, 'FIRSTAPPLICATION/portfolio.html')

def home(request):
    name = "Hello"
    return render(request, 'FIRSTAPPLICATION/home.html')
    # return HttpResponse("Hello, welcome to the Home Page of Nagato Uzumaki")


def about(request):
    return HttpResponse("This is all about Nagato and SixPathsPain")


def contact(request):
    return HttpResponse("contact Nagato here  ")


#  Django ORM --- Object Relational Mapping --> replica of SQL queries

def form_view(request):
    #Template Tagging --> inject python code to html code
    form=forms.Signupform
    return render(request, 'FIRSTAPPLICATION/register.html', {'form':form})





