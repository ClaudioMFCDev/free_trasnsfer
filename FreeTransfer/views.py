from django.shortcuts import render, redirect
from django.contrib import messages

from usuarios.models import Usuario


# views.py



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth import logout
from .forms import FormUser
from django.contrib.auth import get_user_model
User = get_user_model()


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

    return render(request, 'usuarios/registro.html', {'form': form})






