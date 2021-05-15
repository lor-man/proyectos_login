from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


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
            login(request,userSession)
            if(obj):
                if(rol=="A"):
                    return redirect("gestion")

                if(rol=="U"):                   
                    return redirect("homepage")
            else:
                return render(request,'login.html',{'error':"Invalid rol"})
        else:
            return render(request,'login.html',{'error':"Invalid password or username"})
    return render(request,"login.html")

@login_required
def logout_view(request):
    print(request.user.is_authenticated)
    logout(request)
    print(request.user.is_authenticated)
    return redirect("logon")

@login_required
def gestionAgregar(request):
    if request.method=='POST':
        nombre=request.POST['name']
        contr0=request.POST['password0']
        contr1=request.POST['password1']
        cell=request.POST['phone']
        rol=request.POST['rol']
        userProfile0=None
        if(contr0!=contr1):
            return render(request,'gestion.html',{'info':'Las contrasenas no coinciden'})
        if(rol=='Administrador'):
            rol='A'
        elif(rol=='Usuario'):
            rol='U'
        try:
            name=User.objects.get(username=nombre)
            print(name)
            if(name):
                return render(request,'gestion.html',{'info':'El nombre de usuario ya existe'})
        except:
            try:
                user0=User.objects.create(username=nombre,password=make_password(contr0))
                user0.save()
                if cell:
                    userProfile0=UserProfile.objects.create(user=user0,rol=rol,phone=cell)
                else:
                    userProfile0=UserProfile.objects.create(user=user0,rol=rol)
                userProfile0.save()
            except:
                return render(request,'gestion.html',{'info':'No se ha podido guardar el usuario'})
        return render(request,'gestion.html',{'info':'Usuario guardado'}) 
    return render(request,'gestion.html')

@login_required
def gestionEliminar(request):
    if request.method=='POST':
        userProfile=UserProfile.objects.filter(user__id=request.POST['id'])
        return render(request, 'eliminarUsuario.html',{'obj':userProfile,'idElim':request.POST['id']})        
    return render(request,'eliminarUsuario.html')

@login_required
def gestionVer(request):
    try:
        userProfile=UserProfile.objects.all()
        return render(request, 'verUsuario.html',{'obj':userProfile})
    except:
        return render(request,'verUsuario.html')

@login_required
def gestionEliminado(request):
    try: 
        if request.method=='POST':
            userProfile=User.objects.filter(id=request.POST['id']).delete()
            return render(request,'gestion_eliminado.html')
    except:
        return redirect('gesEliminar')

