from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def registro(request):
    return render(request, 'ingreso_cita.html')
    