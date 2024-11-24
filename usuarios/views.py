from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario, Transferencia, MotivoTransferencia
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import FormUser


def register(request):
    if request.method == 'POST':
        form = FormUser(request.POST, request.FILES)
        if form.is_valid():
            # Obtén los datos del formulario
            password = form.cleaned_data['password1']
            user = form.save(commit=False)  # No guarda el usuario todavía

            # Encripta la contraseña
            user.set_password(password)  # Este método encripta la contraseña
            user.save()  # Guarda el usuario

            return redirect('login')  # Redirige a la página de login
    else:
        form = FormUser()

    return render(request, 'registro.html', {'form': form})





def iniciar_sesion(request):
    se_autentico = False
    salio_mal = False
    mensaje_error = ""
    username = ""

    if request.method == "POST":
        username = request.POST.get("username", default=None)
        password = request.POST.get("password", default=None)
        usuario = authenticate(request, username=username, password=password)

        se_autentico = True

        if usuario:
            salio_mal = False
            login_django(request, usuario)
            return redirect("home")
        else:
            salio_mal = True
            mensaje_error = "Credenciales incorrectas. Por favor, verifica tus datos."

    ctx = {
        "se_autentico": se_autentico,
        "salio_mal": salio_mal,
        "mensaje_error": mensaje_error,
        "username": username,
    }

    return render(request, 'login.html', ctx)



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