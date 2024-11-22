from django.shortcuts import render

# Create your views here.
# movimientos/views.py
from django.shortcuts import render, redirect
from .models import Cuenta, MotivoTransferencia, Movimiento
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TransferenciaForm
from .models import Cuenta

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cuenta
# transacciones/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IngresoDineroForm
from .models import Cuenta
from django.contrib.auth import get_user_model
User = get_user_model()






def home(request):
    if request.user.is_authenticated:
        # Intentamos obtener la cuenta asociada al usuario logueado
        try:
            cuenta = Cuenta.objects.get(usuario=request.user)
            saldo = cuenta.saldo
        except Cuenta.DoesNotExist:
            saldo = 0  # Si no existe la cuenta, el saldo será 0
    else:
        saldo = 0  # Si el usuario no está logueado, el saldo será 0

    return render(request, 'home.html', {'saldo': saldo})

def listar_cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'movimientos/listar_cuentas.html', {'cuentas': cuentas})



@login_required
def ingresar_dinero(request):
    if request.method == 'POST':
        form = IngresoDineroForm(request.POST)
        if form.is_valid():
            monto = form.cleaned_data['monto']
            # Obtener la cuenta del usuario autenticado
            cuenta, created = Cuenta.objects.get_or_create(usuario=request.user)
            cuenta.saldo += monto
            cuenta.save()
            Movimiento.objects.create(cuenta_origen=cuenta, cuenta_movimiento=cuenta, tipo="ingreso", monto=monto)
            return redirect('confirmacion_transferencia')  # Redirigir a la página principal o una página de confirmación
    else:
        form = IngresoDineroForm()

        # Guardar el movimiento para historial
    
            

    return render(request, 'ingresar_dinero.html', {'form': form})


@login_required
def realizar_transferencia(request):
    if request.method == 'POST':
        form = TransferenciaForm(request.POST)
        if form.is_valid():
            destinatario_username = form.cleaned_data['destinatario']
            monto = form.cleaned_data['monto']
            motivo = form.cleaned_data['motivo']
            
            # Verificar que el destinatario existe
            try:
                destinatario = User.objects.get(username=destinatario_username)
            except User.DoesNotExist:
                messages.error(request, "El usuario destinatario no existe.")
                return render(request, 'Transferencia.html', {'form': form})

            # Verificar que el remitente tiene saldo suficiente
            remitente_cuenta, _ = Cuenta.objects.get_or_create(usuario=request.user)
            if remitente_cuenta.saldo < monto:
                messages.error(request, "No tienes saldo suficiente para realizar esta transferencia.")
                return render(request, 'Transferencia.html', {'form': form})

            # Obtener o crear la cuenta del destinatario
            destinatario_cuenta, _ = Cuenta.objects.get_or_create(usuario=destinatario)

            # Realizar la transferencia
            remitente_cuenta.saldo -= monto
            remitente_cuenta.save()

            destinatario_cuenta.saldo += monto
            destinatario_cuenta.save()

            # Guardar el movimiento para historial
            Movimiento.objects.create(cuenta_origen=remitente_cuenta, cuenta_movimiento=remitente_cuenta,cuenta_destino=destinatario_cuenta, tipo="transferencia", monto=monto, motivo=motivo)
            Movimiento.objects.create(cuenta_origen=remitente_cuenta, cuenta_movimiento=destinatario_cuenta,cuenta_destino=destinatario_cuenta, tipo="ingreso transferencia", monto=monto, motivo=motivo)

            # Redirigir a una página de confirmación
            return redirect('confirmacion_transferencia')  # Redirigir a una página de confirmación
    else:
        form = TransferenciaForm()

    return render(request, 'Transferencia.html', {'form': form})



def confirmacion_transferencia(request):
    return render(request, 'confirmacion_transferencia.html')


def listar_movimientos(request):

    context={}
    todos= Movimiento.objects.filter(cuenta_movimiento=request.user.cuenta)
    context['movimientos']=todos
    return render(request,'listado.html', context)


