# transacciones/forms.py
from django import forms
from django.contrib.auth.models import User

class IngresoDineroForm(forms.Form):
    monto = forms.DecimalField(max_digits=10, decimal_places=2, label="Monto a ingresar")



from .models import MotivoTransferencia

class TransferenciaForm(forms.Form):
    destinatario = forms.CharField(max_length=150, label="Usuario Destinatario")
    monto = forms.DecimalField(max_digits=10, decimal_places=2, label="Monto")
    motivo = forms.ModelChoiceField(
        queryset=MotivoTransferencia.objects.all(),
        label="Motivo de la Transferencia",
        empty_label="Seleccione un motivo"
    )

