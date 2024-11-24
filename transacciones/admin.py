from django.contrib import admin

# Register your models here.
# movimientos/admin.py
from django.contrib import admin
from .models import Cuenta, MotivoTransferencia, Movimiento, MotivoTransferencia

admin.site.register(Cuenta)

admin.site.register(Movimiento)

