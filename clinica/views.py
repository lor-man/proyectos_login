from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def busqueda_producto(request):
    return render(request,"formulario.html")

def buscar(request):
    mensaje="Articulo buscado: %r"%request.GET["prd1"]
    return HttpResponse(mensaje)