from django.shortcuts import render
from datetime import datetime 
from django.http import HttpResponse

from django.template import Template, loader


def inicio(request):
    return HttpResponse(f"<h1> Bienvenidos al inicio de cande 3ra pre entregsa </h1>")

def template1(request):
    return HttpResponse(f"<h1> mi template 1 cande </h1>")


def template2 (request, nombre, apellido):
    fecha = datetime.now()
    return render(request, "template1.html", fecha, nombre, apellido)
