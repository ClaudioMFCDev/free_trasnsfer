from django.contrib import admin

from .models import Usuario, UsuarioFavorito, MotivoTransferencia

admin.site.register(Usuario)
admin.site.register(UsuarioFavorito)
admin.site.register(MotivoTransferencia)

