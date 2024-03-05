from django.shortcuts import render, get_object_or_404
from .models import *

def inicio(request):
    
    return render(request, "inicio.html")

def nosotros(request):

    return render(request, "nosotros.html")

def admision(request):
    
    return render(request, "admision.html")

def adelanto(request):
    
    return render(request, "adelanto.html")

def nivelacion(request):

    return render(request, "nivelacion.html")

def refuerzo(request):

    return render(request, "refuerzo.html")

def r_esta1(request):
    
    horarios = Horario.objects.filter(imagen__icontains='esta1')

    return render(request, "r_esta1.html", {"horarios":horarios})

def r_esta2(request):
    
    horarios = Horario.objects.filter(imagen__icontains='esta2')

    return render(request, "r_esta2.html", {"horarios":horarios})

def refuerzopre(request):

    return render(request, "refuerzopre.html")
