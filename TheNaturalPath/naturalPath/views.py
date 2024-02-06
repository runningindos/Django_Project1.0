from django.shortcuts import render
from django.http import HttpResponse 
from .models import Providers, Users, Practice

# Create your views here.

def home(request, context):

    context={
        "Providers" : Providers.objects.all()
    }
    return render(request, 'home.html')

    

