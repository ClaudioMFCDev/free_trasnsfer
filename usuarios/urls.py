from django.urls import path
from django.contrib.auth import views as auth_views  # Importa desde django.contrib.auth.views
from . import views

app_name='usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Vista de inicio de sesión
    path('registro/', views.registro, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transferencia/', views.transferencia, name='transferencia'),
    path('ingresar_dinero/', views.ingresar_dinero, name='ingresar_dinero'),
    path('usuarios/', views.listado_usuarios, name='listado_usuarios'),
    


]
