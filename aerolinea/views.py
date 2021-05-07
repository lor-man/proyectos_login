from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from aerolinea.forms import NameForm
# Create your views here.


def boletos(request):
    return render(request,"boletos.html")

def calculo(request):
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

    return render(request,'calculo.html',{'numero':"{:.2f}".format(subTotal),'descuento':"{:.2f}".format(desc),'total':"{:.2f}".format(total),'nombre':request.POST['nombre'],'clase':clss})

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
        
