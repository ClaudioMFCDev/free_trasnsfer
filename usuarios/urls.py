
from django.urls import path

from . import views
from .views import UsuarioDeleteView, EditarPerfilView


app_name = 'usuarios'

urlpatterns = [
    #path('transferencia/', views.transferencia, name='transferencia'),
    path('ingresar_dinero/', views.ingresar_dinero, name='ingresar_dinero'),
    path('ingresar_dinero/confirmacion', views.confirmacion, name='ingresar_dinero'),
    path('realizar_transferencia/', views.realizar_transferencia, name='realizar_transferencia'),
    path('realizar_transferencia/ingresar_monto_transferencia/', views.ingresar_monto_transferencia, name='ingresar_monto_transferencia'),
   	path('realizar_transferencia/ingresar_monto_transferencia/confirmacion', views.confirmacion, name='confirmar_transferencia'),  # Página de confirmación
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('tudinero', views.tudinero, name='tudinero'),
    path('tuactividad', views.tuactividad, name='tuactividad'),
    # path('login/', views_django.LoginView.as_view(template_name="login.html"), name='login'),
    path('favoritos/', views.Listar.as_view(), name='favoritos'),
    # eliminar fav
    path('eliminar_favorito/<int:usuario_favorito_id>/', views.eliminar_favorito, name='eliminar_favorito'),
    # detalle vacuna
    path('usuario/<int:pk>/', views.UsuarioPerfil.as_view(), name='perfil'),
    path('perfil/editar/', EditarPerfilView.as_view(), name='editar_perfil'),

    path('eliminar/<int:pk>/',UsuarioDeleteView.as_view(), name='eliminar_usuario'),
    path('listado_usuarios/', views.listar_usuarios,name='listado_usuarios'),
    path('movimiento_por_usuario/<int:pk>/', views.Listar_MovimientosPorUsuario,name='movimiento_por_usuario'),
    path('usuariodenegadp/', views.Listar_MovimientosPorUsuario, name='usuariodenegadp'),

    #path('editar_perfil/<str:pk>', views.EditarPerfil_clase.as_view(template_name= "editarperfil.html"), name='editar_perfil' ),
    # path('editar_perfil/<str:pk>/', views.EditarPerfil_clase.as_view(), name='editar_perfil'),
    path('activar_usuario/<str:pk>/', views.activar_usuario.as_view(), name='activar_usuario'),
    

]





 