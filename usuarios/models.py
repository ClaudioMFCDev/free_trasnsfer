
from django.contrib.auth.models import AbstractUser, BaseUserManager  # Asegúrate de importar BaseUserManager
from django.core.exceptions import ValidationError

from django.db import models

class Solicitud(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo



class Usuario(AbstractUser):
    dni = models.IntegerField(null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.id} -- {self.username}  --  {self.first_name} --  {self.last_name}"



class UsuarioFavorito(models.Model):
    usuario_origen = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name="favoritos_origen"
    )
    
    usuario_favorito = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name="es_favorito_de"
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario_origen', 'usuario_favorito'], 
                name='unique_favorito'
            )
        ]

    def clean(self):
        # Evitar que un usuario se agregue a sí mismo como favorito
        if self.usuario_origen == self.usuario_favorito:
            raise ValidationError("No puedes agregarte a ti mismo como favorito.")
    
    def save(self, *args, **kwargs):
        self.full_clean()  # Llama a las validaciones antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Usuario origen: {self.usuario_origen} -- Usuario Favorito: {self.usuario_favorito}"



class Transferencia(models.Model):
    usuario_origen = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transferencias_realizadas')
    usuario_destino = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transferencias_recibidas')
    motivo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)



class MotivoTransferencia(models.Model):
    nombre = models.CharField(max_length=100)
    
