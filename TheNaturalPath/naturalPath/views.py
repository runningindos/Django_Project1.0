from django.shortcuts import render
from django.http import HttpResponse 
from .models import Providers, Users, Practice
from django.shortcuts import render

# Create your views here.

def home(request, ):
    return render(request, 'home.html')

def providers(request, ):
    context = {

        'providers' : providers
    }
    return render(request, 'providers.html', context)
 
def register(request, ):
    return render(request,'register.html')

def login(request, ):
    return render(request, 'login.html')

def logout(request, ):
    return render(request, 'logout.html')

def success(request, ):
    return render(request,'success.html')


Providers = [
    {
        'first_name': 'Caoidhreach',
        'last_name': 'Mac hAidhearais',
        'email': '<ricky@ricky.com>',
    },
    {
        'first_name': 'George',
        'last_name': 'Mahony',
        'email': '<george@george.com>',
    },
    {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'email': '<jane@jane.com>',
    }
]
