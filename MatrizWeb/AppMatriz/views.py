from django.shortcuts import render, get_object_or_404
from .models import *

def inicio(request):
    
    return render(request, "inicio.html")

def refuerzo_pre(request):

    return render(request, "refuerzo_pre.html")

def adm_up(request):
    
    return render(request, "adm_up.html")

def adm_regular(request):
    
    return render(request, "adm_regular.html")

def adm_selectiva(request):
    
    return render(request, "adm_selectiva.html")

def adelanto(request):
    
    return render(request, "adelanto.html")

def nivelacion(request):

    return render(request, "nivelacion.html")

def nosotros(request):

    return render(request, "nosotros.html")

def refuerzo_up(request):

    return render(request, "refuerzo_up.html")

"""
===============================
CURSOS REFUERZO UNIVERSITARIO
===============================
"""

def nive_mate(request):
    
    horarios = Horario.objects.filter(imagen__icontains='nive_mate')

    return render(request, "r_nive_mate.html", {"horarios":horarios})

def mate1(request):
    
    horarios = Horario.objects.filter(imagen__icontains='mate1')

    return render(request, "r_mate1.html", {"horarios":horarios})

def mate2(request):
    
    horarios = Horario.objects.filter(imagen__icontains='mate2')

    return render(request, "r_mate2.html", {"horarios":horarios})

def mate_nego(request):
    
    horarios = Horario.objects.filter(imagen__icontains='mate_nego')

    return render(request, "r_mate_nego.html", {"horarios":horarios})

def mate3(request):
    
    horarios = Horario.objects.filter(imagen__icontains='mate3')

    return render(request, "r_mate3.html", {"horarios":horarios})

def r_esta1(request):
    
    horarios = Horario.objects.filter(imagen__icontains='esta1')

    return render(request, "r_esta1.html", {"horarios":horarios})

def r_esta2(request):
    
    horarios = Horario.objects.filter(imagen__icontains='esta2')

    return render(request, "r_esta2.html", {"horarios":horarios})

def amn(request):
    
    horarios = Horario.objects.filter(imagen__icontains='amn')

    return render(request, "r_amn.html", {"horarios":horarios})

def nive_info(request):
    
    horarios = Horario.objects.filter(imagen__icontains='nive_info')

    return render(request, "r_nive_info.html", {"horarios":horarios})

def analisis(request):
    
    horarios = Horario.objects.filter(imagen__icontains='analisis')

    return render(request, "r_analisis.html", {"horarios":horarios})

def eco1(request):
    
    horarios = Horario.objects.filter(imagen__icontains='eco1')

    return render(request, "r_eco1.html", {"horarios":horarios})

def eco2(request):
    
    horarios = Horario.objects.filter(imagen__icontains='eco2')

    return render(request, "r_eco2.html", {"horarios":horarios})

def funda_finanzas(request):
    
    horarios = Horario.objects.filter(imagen__icontains='funda_finanzas')

    return render(request, "r_funda_finanzas.html", {"horarios":horarios})

def nive_lengua(request):
    
    horarios = Horario.objects.filter(imagen__icontains='nive_lengua')

    return render(request, "r_nive_lengua.html", {"horarios":horarios})

def lengua1(request):
    
    horarios = Horario.objects.filter(imagen__icontains='lengua1')

    return render(request, "r_lengua1.html", {"horarios":horarios})

def lengua2(request):
    
    horarios = Horario.objects.filter(imagen__icontains='lengua2')

    return render(request, "r_lengua2.html", {"horarios":horarios})