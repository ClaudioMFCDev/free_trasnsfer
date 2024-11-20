"""
URL configuration for FreeTransfer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar 'include'
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .forms import RegistroForm  # Esta es la importación correcta


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/login/registro/', views.registro, name='registro'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tudinero', views.tudinero, name='tudinero'),
    path('tuactividad', views.tuactividad, name='tuactividad'),

    # URLs de Aplicaciones

    path('realizar_transferencia/', views.realizar_transferencia, name='realizar_transferencia'),
    path('realizar_transferencia/ingresar_monto_transferencia/', views.ingresar_monto_transferencia, name='ingresar_monto_transferencia'),
    path('realizar_transferencia/ingresar_monto_transferencia/confirmacion', views.confirmacion, name='confirmar_transferencia'),  # Página de confirmación
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('ingresar_dinero/', views.ingresar_dinero, name='ingresar_dinero'),
    path('ingresar_dinero/confirmacion', views.confirmacion, name='ingresar_dinero'),

]


