from django.shortcuts import render
from django.http import HttpResponse 
from .models import Providers, Users, Practice

# Create your views here.

def home(request, ):
    return render(request, 'home.html')

    

