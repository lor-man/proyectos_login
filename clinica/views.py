from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from clinica.models import paciente
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def registro(request):
    if request.method=='POST':
        paciente_nuevo=paciente(
            nombre=request.POST['nombre'],
            edad=request.POST['edad'],
            peso=request.POST['peso'],
            altura=request.POST['altura'],
            fecha=request.POST['fecha'],
            hora=request.POST['hora']
        )
        paciente_nuevo.save()

    return render(request, 'ingreso_cita.html')
@login_required
def registros(request):
    if request.method=='POST':
        fecha_consulta=request.POST['fecha']
        print(fecha_consulta)
        citas_consultadas=paciente.objects.filter(fecha=fecha_consulta)
        return render(request,'citas_dia.html',{'citas_consultadas':citas_consultadas})

    return render(request, 'citas_dia.html')
@login_required
def eliminar(request):
    if request.method=='POST':
        cita_eliminar=paciente.objects.filter(fecha=request.POST['fecha'])
        fech=cita_eliminar[0].fecha
        return render(request,'cita_eliminacion.html',{'fecha':cita_eliminar,'fch':fech})
    return render(request, 'cita_eliminacion.html')
@login_required
def eliminado(request):
    if request.method=='POST':
        registro=paciente.objects.filter(pk=request.POST['idd']).delete()
        return render(request,'cita_eliminada.html')


