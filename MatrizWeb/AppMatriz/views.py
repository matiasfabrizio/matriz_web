from django.shortcuts import render, get_object_or_404
from .models import *

def inicio(request):
    
    return render(request, "inicio.html")

def admision(request):
    
    return render(request, "admision.html")

def refuerzo(request):
    
    return render(request, "refuerzo.html")

def refuerzo_cursos(request, codigo_curso):
    cursos = get_object_or_404(Curso, codigo=codigo_curso)

    if codigo_curso == 'esta1':

        return render(request, 'r_esta1.html', {'curso': cursos})
    
    elif codigo_curso == 'esta2':

        return render(request, 'r_esta2.html', {'curso': cursos})
