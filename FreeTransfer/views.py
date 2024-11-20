from django.shortcuts import render, redirect
from django.contrib import messages

from usuarios.models import Usuario


# views.py



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth import logout
from .forms import RegistroForm

# Vista para el home del usuario registrado
@login_required
def home(request):
    # Obtener el importe de la sesión, si está disponible
    importe = request.session.get('importe', 0)
    return render(request, 'usuarios/home.html', {'importe': importe})

#def exit(request):
 #	loguot(request)
 #	return redirect('usuarios/registration.login.html')


def registro(request):
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

    return render(request, 'usuarios/registro.html', {'form': form})





def tudinero(request):
    # Obtener el importe de la sesión, si está disponible
    importe = request.session.get('importe', 0)
    return render(request, 'usuarios/tu_dinero.html', {'importe': importe})


def tuactividad(request):
    
    return render(request, 'usuarios/tu_actividad.html')


def ingresar_dinero(request):
        
    return render(request, 'usuarios/ingresar_dinero.html')


def realizar_transferencia(request):
    
    return render(request, 'usuarios/tranferencia.html')

def ingresar_monto_transferencia(request):
        
    return render(request, 'usuarios/monto_tranferencia.html')


def confirmacion(request):
    # Tu lógica para manejar la transferencia
    return render(request, 'usuarios/confirmacion.html')
