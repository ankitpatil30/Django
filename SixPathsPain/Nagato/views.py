from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, welcome to the Home Page of Nagato")


def about(request):
    return HttpResponse("This is all about Nagato and SixPathsPain")


def contact(request):
    return HttpResponse("contact Nagato here  ")