
# Create your models here.
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    nombre = models.CharField(
        'Nombre',
        max_length=50
    )
    email = models.EmailField(
        'Email'
    )
    comentario = models.TextField(
        'Comentario que ha dejado en la web'
    )
    created_at = models.DateTimeField(
        'Fecha de creacion',
        default=timezone.now
    )
    contactado = models.BooleanField(
        '¿Se ha contactado con él?',
        default=False
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'