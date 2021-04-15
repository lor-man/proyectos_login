from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
def logon(request):
    if(request.method == "POST"):
        username = request.POST('username')
        password = request.POST('password')
        userSession = authenticate(request, username=username,password=password)
        if(userSession):
            login(request, userSession)
            return redirect('homepage')
        else:
            return render(request,'index.html',{'error':"Invalid password"})
    return render(request,"index.html")
