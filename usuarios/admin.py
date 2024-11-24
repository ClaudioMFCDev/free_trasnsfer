from django.contrib import admin

from .models import Usuario, UsuarioFavorito

admin.site.register(Usuario)
admin.site.register(UsuarioFavorito)