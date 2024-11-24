from django.conf import settings
from django.conf.urls.static import static

# FreeTransfer/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as views_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/login/registro/', views.registro, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('usuarios/', include("usuarios.urls")),



    # Incluir las rutas de la app transacciones
    path('transacciones/', include('transacciones.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

