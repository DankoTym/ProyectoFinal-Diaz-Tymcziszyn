from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Inicio(self):
    plantilla = loader.get_template('AppSuper/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
