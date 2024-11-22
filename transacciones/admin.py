from django.contrib import admin

# Register your models here.
# movimientos/admin.py
from django.contrib import admin
from .models import Cuenta, MotivoTransferencia, Movimiento

admin.site.register(Cuenta)
admin.site.register(MotivoTransferencia)
admin.site.register(Movimiento)
