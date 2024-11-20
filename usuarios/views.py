from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario, Transferencia, MotivoTransferencia
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistroForm


def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            # Obtén los datos del formulario
            password = form.cleaned_data['password1']
            user = form.save(commit=False)  # No guarda el usuario todavía

            # Encripta la contraseña
            user.set_password(password)  # Este método encripta la contraseña
            user.save()  # Guarda el usuario

            return redirect('login')  # Redirige a la página de login
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})




def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Inicia la sesión del usuario
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirige a la página del dashboard
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from .forms import TransferenciaForm
from .models import Transferencia, Usuario
from django import forms


def tudinero(request):
    # Obtener el importe de la sesión, si está disponible
    importe = request.session.get('importe', 0)
    return render(request, 'tu_dinero.html', {'importe': importe})

def tuactividad(request):
    
    return render(request, 'tu_actividad.html')


def ingresar_dinero(request):
        
    return render(request, 'ingresar_dinero.html')


def realizar_transferencia(request):
    
    return render(request, 'transferencia.html')

def ingresar_monto_transferencia(request):
        
    return render(request, 'monto_tranferencia.html')


def confirmacion(request):
    # Tu lógica para manejar la transferencia
    return render(request, 'confirmacion.html')