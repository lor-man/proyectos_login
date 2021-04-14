from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def logon(request):
    return HttpResponse("Pagina formulario de ingreso")
