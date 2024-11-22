

from django.urls import path


from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.registro, name='registro'),
    path('transferencia/', views.transferencia, name='transferencia'),
    path('ingresar_dinero/', views.ingresar_dinero, name='ingresar_dinero'),
    path('ingresar_dinero/confirmacion', views.confirmacion, name='ingresar_dinero'),
    path('realizar_transferencia/', views.realizar_transferencia, name='realizar_transferencia'),
    path('realizar_transferencia/ingresar_monto_transferencia/', views.ingresar_monto_transferencia, name='ingresar_monto_transferencia'),
   	path('realizar_transferencia/ingresar_monto_transferencia/confirmacion', views.confirmacion, name='confirmar_transferencia'),  # Página de confirmación
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('tudinero', views.tudinero, name='tudinero'),
    path('tuactividad', views.tuactividad, name='tuactividad'),
    path('login/', views_django.LoginView.as_view(template_name="login.html"), name='login'),

]





 