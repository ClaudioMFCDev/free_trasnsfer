from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario, Transferencia, MotivoTransferencia
from django.contrib.auth.forms import UserCreationForm





def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

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

@login_required
def dashboard(request):
    saldo = request.user.saldo
    transferencias = Transferencia.objects.filter(usuario_origen=request.user).order_by('-fecha')
    return render(request, 'usuarios/dashboard.html', {'saldo': saldo, 'transferencias': transferencias})

@login_required
def transferencia(request):
    if request.method == 'POST':
        usuario_destino = request.POST.get('usuario_destino')
        motivo = request.POST.get('motivo')
        monto = request.POST.get('monto')
        
        # Implementa la lógica para realizar la transferencia aquí
        
    motivos = MotivoTransferencia.objects.all()
    return render(request, 'usuarios/transferencia.html', {'motivos': motivos})

@login_required
def ingresar_dinero(request):
    # Lógica para ingresar dinero
    pass

@login_required
def listado_usuarios(request):
    if request.user.es_admin:
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios/listado_usuarios.html', {'usuarios': usuarios})
    else:
        return redirect('dashboard')




