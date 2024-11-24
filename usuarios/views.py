from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario, Transferencia, MotivoTransferencia
from transacciones.models import Cuenta, Movimiento
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, MotivoTransferencia
from transacciones.models import Cuenta



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import FormUser, EditarPerfil, ActivarUsuario
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView 
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages






from django.contrib.auth import authenticate, login as login_django
from django.shortcuts import render, redirect

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

#class EditarPerfil_clase(UpdateView):
#    model = Usuario
#    form_class = EditarPerfil
#    template_name = 'usuarios/editarperfil.html'
#    success_url = reverse_lazy('home')

#    def form_valid(self, form):
        
#        perfil = form.save(commit = False)
        
#        perfil.save()

 #       return redirect(self.success_url)
def is_staff(user):
    return user.is_staff

class EditarPerfil_clase(UpdateView):
    model = Usuario
    form_class = EditarPerfil
    template_name = 'usuarios/editarperfil.html'

    def get_success_url(self):
        # Verificar si el usuario es parte del personal (is_staff)
        if self.request.user.is_staff:
            return reverse_lazy('usuarios:listado_usuarios')  # Redirigir a listado de usuarios si es staff
        else:
            return reverse_lazy('home')  # Redirigir al home si no es staff

    def form_valid(self, form):
        perfil = form.save(commit=False)
        
        perfil.save()
        return redirect(self.get_success_url())  # Usar el método get_success_url para redirigir

class activar_usuario(UpdateView):
    model = Usuario
    form_class = ActivarUsuario
    template_name = 'usuarios/activar_usuario.html'
    success_url = reverse_lazy('usuarios:listado_usuarios')

    # Redirigir al home si no es staff

    def form_valid(self, form):
        perfil = form.save(commit=False)
        perfil.save()
        return redirect(self.get_success_url())  # Usar el método get_success_url para redirigir

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/confirmacion_eliminar_usuario.html'
    success_url = reverse_lazy('usuarios:listado_usuarios')  # Redirige tras eliminar

def listar_usuarios(request):
    if not request.user.is_staff:
        messages.error(request, "No tienes permisos para acceder a esta página.")
        return render(request, 'usuarios/denegado.html')
    context={}
    todos=Usuario.objects.all() #MotivoTransferencia.objects.all()
    context['usuarios']=todos
    return render(request,'usuarios/listado_usuarios.html', context)
    if not request.user.is_staff:
        messages.error(request, "No tienes permisos para acceder a esta página.")
        return render(request, 'usuarios/denegado.html')



#@user_passes_test(is_staff)
def Listar_MovimientosPorUsuario(request, pk):
    # Verificar si el usuario no es staff
    if not request.user.is_staff:
        messages.error(request, "No tienes permisos para acceder a esta página.")
        return render(request, 'usuarios/denegado.html')
    # Obtener el usuario directamente por el pk (ID del usuario)
    usuario = Usuario.objects.get(pk=pk)
    
    # Obtener la cuenta del usuario
    cuenta = Cuenta.objects.get(usuario=usuario)
    
    # Obtener los movimientos de la cuenta
    movimientos = Movimiento.objects.filter(cuenta_origen=cuenta) | Movimiento.objects.filter(cuenta_destino=cuenta)
    
    # Pasar los movimientos a la plantilla
    context = {
        'usuario': usuario,
        'movimientos': movimientos
    }
    
    return render(request, 'usuarios/movimientos_por_usuario.html', context)




