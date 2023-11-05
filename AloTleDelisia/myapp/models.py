from django.db import models

# Create your models here.

class Usuario(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=15)
    apellidos=models.TextField()
    fecha_nac = models.DateField('Fecha de nacimiento')
    correo=models.EmailField()
    direccion=models.TextField()
    contrasenya = models.CharField(max_length=255, default='a')
