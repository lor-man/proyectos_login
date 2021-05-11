from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from aerolinea.forms import NameForm
from aerolinea.models import boletoAerolinea
# Create your views here.


def boletos(request):
    return render(request,"boletos.html")

def calculo(request):
    try:
        if request.method=='POST':
            cont=0
            desc=0.0
            total=0
            clss=""
            com1=request.POST['cm1']
            com2=request.POST['cm2']
            com3=request.POST['cm3']
            
            beb1=request.POST['beb1']
            beb2=request.POST['beb2']
            beb3=request.POST['beb3']
            
            pl1=request.POST['pl1']
            pl2=request.POST['pl2']
            pl3=request.POST['pl3']

            com=[int(com1),int(com2),int(com3)]
            beb=[int(beb1),int(beb2),int(beb3)]
            pl=[int(pl1),int(pl2),int(pl3)]
            
            subCom=50*int(com1)+40*int(com2)+25*int(com3)
            subBeb=35*int(beb1)+25*int(beb2)+10*int(beb3)
            subPel=70*int(pl1)+55*int(pl2)+25*int(pl3)
            subTotal=float(subBeb+subCom+subPel)
            clss1=int(com[0])+int(beb[0])+int(pl[0])
            clss2=int(com[1])+int(beb[1])+int(pl[1])
            clss3=int(com[2])+int(beb[2])+int(pl[2])
            
            for cnt in com:
                cont=cont+cnt
            for cnt in beb:
                cont=cont+cnt
            for cnt in pl:
                cont=cont+cnt
            
            if(cont>=10 and com[0]>=1 and beb[0]>=1 and pl[0]>=1):
                desc= 0.15*subTotal
            elif(com[0]>=1 and beb[0]>=1 and pl[0]>=1 and com[1]==com[2]==beb[1]==beb[2]==pl[1]==pl[2]==0):
                desc= 0.05*subTotal
            elif(cont>=10):
                desc= 0.1*subTotal
            else:
                desc=0
            total=subTotal-desc   

            if(request.POST["clssVuelo"]=="1"):
                clss="Primera clase"
            elif(request.POST["clssVuelo"]=="2"):
                clss="Segunda clase"
            elif(request.POST["clssVuelo"]=="3"):
                clss="Tercera clase"
            
            objMod=boletoAerolinea(
                nombre=request.POST['nombre'],
                vuelo=int(request.POST["clssVuelo"]),
                srcClss1=clss1,
                srcClss2=clss2,
                srcClss3=clss3,
                subTotal= subTotal,
                descuento=desc,
                total=total
            )
            objMod.save()
            return render(request,'calculo.html',{'numero':"{:.2f}".format(subTotal),'descuento':"{:.2f}".format(desc),'total':"{:.2f}".format(total),'nombre':request.POST['nombre'],'clase':clss})
        else:
            return render(request,'calculo.html',{'numero':"--",'descuento':"--",'total':"--",'nombre':"--",'clase':"--"})
    except Exception as exc:
        print(str(exc))
        return render(request,'calculo.html',{'numero':"--",'descuento':"--",'total':"--",'nombre':"--",'clase':"--"})
        
def get_name(request):
    form=NameForm()   
    print(form)
    return render(request,'name.html',{'form':NameForm()})

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

def registro(request):
    obj=boletoAerolinea.objects.all()
    return render(request,'registro.html',{'boleto':obj})

def reg_eliminar(request):
    if request.method=='POST':
        if(request.POST["reg"]):
            print("reg")
            idd=request.POST["reg"]
            obj=boletoAerolinea.objects.filter(pk=int(idd))
            return render(request,'reg_eliminar.html',{'rg':obj})
    print("aqui")
    return render(request, 'reg_eliminar.html')

def limpiar(request):
    if request.method=='POST':
        idd=request.POST["id"]
        obj=boletoAerolinea.objects.filter(pk=int(idd)).delete()
        return render(request,'registro_eliminado.html')
    else:
        return redirect('boleto')



        
