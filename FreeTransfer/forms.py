# forms.py
from django import forms

from django.db import models
from django import forms
from usuarios.models import Usuario 
from django.contrib.auth.forms import UserCreationForm
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

