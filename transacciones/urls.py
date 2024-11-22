# movimientos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingresar_dinero/', views.ingresar_dinero, name='ingresar_dinero'),
    path('realizar_transferencia/', views.realizar_transferencia, name='realizar_transferencia'),
    path('confirmacion_transferencia/', views.confirmacion_transferencia, name='confirmacion_transferencia'),
    path('listar_movimientos/', views.listar_movimientos ,name='listar_movimientos'),
    



    #path('realizar_transferencia/', views.realizar_transferencia, name='realizar_transferencia'),
]