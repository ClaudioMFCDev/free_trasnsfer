from django.db import models

# Create your models here.
# movimientos/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings



class Cuenta(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.usuario.username} - ${self.saldo}"


class MotivoTransferencia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Movimiento(models.Model):
    TIPO_MOVIMIENTO = [
    ('ingreso', 'Ingreso'),
    ('transferencia', 'Transferencia'),
    ('ingresotransferencia', 'Ingreso  por Transferencia')
]

    cuenta_movimiento=models.ForeignKey(
        Cuenta, on_delete=models.CASCADE, related_name='cuenta', null=True, blank=True
    )
    cuenta_origen = models.ForeignKey(
        Cuenta, on_delete=models.CASCADE, related_name='cuenta_origen', null=True, blank=True
    )
    cuenta_destino = models.ForeignKey(
        Cuenta, on_delete=models.CASCADE, related_name='cuenta_destino', null=True, blank=True
    )
    tipo = models.CharField(max_length=30, choices=TIPO_MOVIMIENTO)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    motivo = models.ForeignKey(MotivoTransferencia, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto} ({self.cuenta_origen} -> {self.cuenta_destino})"


