from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader

def test01(self):
    
    diccionario = {}

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)