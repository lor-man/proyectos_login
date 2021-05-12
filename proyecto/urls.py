"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from proyecto import views as general
from users import views as users
from clinica import views as clinica
from aerolinea import views as aero

urlpatterns = [
    path('', general.homepage, name = "homepage"),
    path('admin/', admin.site.urls, name = "administration"),
    path('login/', users.logon, name = "logon"),
    path('logout/',users.logout_view,name="logout"),
    path('calc-boleto/',aero.boletos,name="boleto"),
    path('calc-boleto/calculo',aero.calculo,name="calculo"),
    path('calc-boleto/registros',aero.registro,name="registros"),
    path('calc-boleto/eliminar-registro',aero.reg_eliminar,name="eliminar"),
    path('calc-boleto/registro-a-eliminar',aero.limpiar,name="limpiar"),
    path('clinica-registro/',clinica.registro,name="registro"),
    path('clinica/registros',clinica.registros,name="registros"),
    path('clinica/eliminar-registro', clinica.eliminar,name="eliminar"),
    path('clinica/eliminado',clinica.eliminado,name="eliminado")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
