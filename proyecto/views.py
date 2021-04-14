
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Pagina principal de proyecto")