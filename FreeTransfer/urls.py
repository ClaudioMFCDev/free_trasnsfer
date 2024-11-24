from django.conf import settings
from django.conf.urls.static import static

# FreeTransfer/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as views_django
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.views import LoginView
from transacciones.views import MotivoDeleteView,MotivoCreateView,ingresar_dinero,realizar_transferencia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views_django.LoginView.as_view(template_name="login.html"), name='login'),
    path('accounts/login/registro/', views.registro, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),


    # Incluir las rutas de la app transacciones
    path('transacciones/', include('transacciones.urls')),
    path('usuarios/', include('usuarios.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

