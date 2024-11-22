# forms.py
from django import forms
from .models import Transferencia
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

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

class FormUser(UserCreationForm):
    
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre de usuario'}))
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "is_active", "dni"]
    
    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)

        add_class_form_control = ["first_name", "username", "last_name", "email", "dni", "password1", "password2"]
        
        for attr_field in add_class_form_control:
            self.fields[attr_field].widget.attrs["class"] = "form-control"
    
    # creamos una nueva validación la cual se incorpora a los ya activos en el form
    def clean_dni(self):
        dni = self.cleaned_data["dni"]
        if not ( 7 <= len(str(dni)) <= 8 ):
            raise ValidationError("Dni debe contener entre 7 y 8 caracteres")
        return dni

