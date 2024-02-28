from django.shortcuts import render, get_object_or_404
from .models import *

def inicio(request):
    
    return render(request, "inicio.html")

def admision(request):
    
    return render(request, "admision.html")

def refuerzo(request):
    
    return render(request, "refuerzo.html")

def esta1(request):

    return render(request, "c_esta1.html")