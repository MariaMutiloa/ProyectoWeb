from django.contrib.auth.hashers import check_password
from django.db import models

class Usuario(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=15)
    apellidos = models.TextField()
    fecha_nac = models.DateField('Fecha de nacimiento')
    correo = models.EmailField(unique=True)
    direccion = models.TextField()
    password = models.CharField(max_length=128)  # Campo más largo para almacenar hash

    def verificar_contrasena(self, raw_password):
        # Verifica una contraseña sin necesidad de guardar el modelo
        return check_password(raw_password, self.password)






