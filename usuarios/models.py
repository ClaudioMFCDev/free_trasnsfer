from django.db import models

# Create your models here.


from django.db import models

class Solicitud(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


class Usuario(AbstractUser):
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    es_admin = models.BooleanField(default=False)
    estado=models.BooleanField(default=False)

      # Se agrega el related_name a las relaciones groups y user_permissions
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='usuarios',  # Evita el conflicto de nombre con 'auth.User.groups'
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='usuarios',  # Evita el conflicto de nombre con 'auth.User.user_permissions'
        blank=True
    )




class Transferencia(models.Model):
    usuario_origen = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transferencias_realizadas')
    usuario_destino = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transferencias_recibidas')
    motivo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)



class MotivoTransferencia(models.Model):
    nombre = models.CharField(max_length=100)
    
