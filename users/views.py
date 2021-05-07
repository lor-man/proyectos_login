from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
# Create your views here.
def logon(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        userSession = authenticate(request, username=username,password=password)
        if(userSession):
            login(request, userSession)
            return redirect("homepage")
        else:
            return render(request,'login.html',{'error':"Invalid password or username"})
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("logon")



