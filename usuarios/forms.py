# forms.py
from django import forms
from .models import Transferencia

class TransferenciaForm(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ['usuario_destino', 'monto', 'motivo']
        widgets = {
            'usuario_destino': forms.Select(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control'}),
        }


from django import forms

class IngresoDineroForm(forms.Form):
    importe = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Importe a ingresar',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el importe'})
    )


from django import forms

from django.core.exceptions import ValidationError

class RegistroForm(forms.ModelForm):
    # Campo para la foto de perfil
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    
    # Campo para el saldo inicial
    saldo_inicial = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # Campos de usuario y correo ya vienen del modelo User
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    # Contraseña
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'email', 'saldo', 'foto_perfil'] 
    
    # Validación de contraseñas
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return password2


