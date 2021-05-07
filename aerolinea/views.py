from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from aerolinea.forms import NameForm
# Create your views here.


def boletos(request):
    return render(request,"boletos.html")

def calculo(request):
    mensaje="Cantidad de comida de 2da clase: %r"%request.GET["prd1"]
    return HttpResponse(mensaje)

def get_name(request):
    form=NameForm()   
    return render(request,'name.html',{'form':form})

def name(request):
    if request.method== 'POST':
        nombre=request.POST['your_name']
        msn="Tu nombre es: "+ str(nombre)
        print(msn)
        return HttpResponse(msn)
    else:
        nombre=request.GET['your_name']
        msn="Tu nombre es: "+ str(nombre)
        return HttpResponse(msn)
    return redirect("nombre")
        
