from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, UpdateView, DetailView
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_django

from .models import UsuarioFavorito, Usuario, Transferencia, MotivoTransferencia
from .forms import FormUser

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .forms import EditarPerfilForm



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


# @login_required
class Listar(TemplateView):
    template_name = 'usuarios/favoritos.html'
    # model = UsuarioFavorito
    context_object_name = "usuario"
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # Obtener el usuario actual basado en el pk de la URL
        # usuario_origen_id = self.kwargs.get('pk')
        # usuario = get_object_or_404(Usuario, id=usuario_origen_id)
        usuario = self.request.user

        # Filtrar favoritos para este usuario
        ctx['favoritos'] = UsuarioFavorito.objects.filter(usuario_origen=usuario)
        ctx["titulo"] = "LISTA DE FAVORITOS"
        return ctx


class UsuarioPerfil(DetailView):
    model = Usuario
    template_name = 'usuarios/perfil.html'
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = Usuario.objects.filter(id=self.object.id)
        return context




class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = EditarPerfilForm
    template_name = 'usuarios/editar_perfil.html'
    def get_success_url(self):
        # Redirige al perfil del usuario logueado
        return reverse_lazy('usuarios:perfil', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        print("Usuario que edita:", self.request.user)  # Depuración

        # Retorna el usuario logueado para que edite su propio perfil
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Formulario generado:", context.get("form"))
        return context
