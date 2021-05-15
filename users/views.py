from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from users.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def logon(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        rol = request.POST['rol']
        if(rol=='Administrador'):
            rol="A"
        elif(rol=='Usuario'):
            rol="U"
        userSession = authenticate(request, username=username,password=password)
        if(userSession):
            obj=UserProfile.objects.filter(user__username=username,rol=rol)
            if(obj):
                #print(obj[0].user)
                #print(obj[0].rol)
                #print(obj[0].pk)
                #print(request.user.is_authenticated)
                if(rol=="A"):
                    return redirect("gestion")

                if(rol=="U"):                   
                    return redirect("homepage")
            else:
                return render(request,'login.html',{'error':"Invalid rol"})
        else:
            return render(request,'login.html',{'error':"Invalid password or username"})
    #print(request.user.is_authenticated)
    return render(request,"login.html")

def logout_view(request):
    print(request.user.is_authenticated)
    logout(request)
    print(request.user.is_authenticated)
    return redirect("logon")

def gestionAgregar(request):
    return render(request,'gestion.html')

def gestionEliminar(request):
    return render(request,'eliminarUsuario.html')
def gestionVer(request):
    return render(request,'verUsuario.html')



