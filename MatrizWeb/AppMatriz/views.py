from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from .models import *

def inicio(request):
    
    return render(request, "inicio.html")

def cursos(request):
    
    return render(request, "cursos.html")

def profesores(request):
    
    return render(request, "profesores.html")