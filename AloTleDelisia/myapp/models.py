from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group, Permission


class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    importePedido = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_restaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE)

class TipoRestaurante(models.Model):
    idTipoRestaurante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)


class Restaurante(models.Model):
    idRestaurante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    horario = models.CharField(max_length=255)
    descripcion = models.TextField()
    idTipoRestaurante = models.ForeignKey(TipoRestaurante, on_delete=models.CASCADE)


class TipoProducto(models.Model):
    idTipoProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion=models.TextField()
    idRestaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcionProducto = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    idTipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    idRestaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE)


class Menu(models.Model):
    idMenu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    idTipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

class PedidoProducto(models.Model):
    idPedidoProducto = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()



#Clase con metodos para creacion de usuarios, tanto normales como superUsers.
#Basicamente, el administrador de modelo CustomUser

class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, dni, fecha_nacimiento, password=None):
        if not username:
            raise ValueError('El campo de nombre de usuario es obligatorio')
        email = self.normalize_email(extra_fields.get('email'))
        user = self.model(username=username, first_name=first_name, last_name=last_name, dni=dni, fecha_nacimiento=fecha_nacimiento) #Crea una instancia del usuario con los valores proporcionados
        user.set_password(password) #Cifrado de contraseña antes de almacenarla
        user.save(using=self._db) #Guarda en la base de datos el usuario (base de datos correcta)
        return user

        #Metodo para crear un superuser que utiliza el create_user pero cambiando los permisos a True
    def create_superuser(self, username, first_name, last_name, dni, fecha_nacimiento, password=None): 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, first_name, last_name, dni, fecha_nacimiento, password)


#AbstractUser para la creacion de un modelo con campos a nuestro gusto
#PermissionsMixin para todo lo relacionado con permisos y autorizaciones

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField() #Formato: YYYY-MM-DD
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True) #Para dar permiso a que entre en el sitio de administracion
    groups = models.ManyToManyField(Group, verbose_name='grupos', blank=True, help_text='Los grupos a los que pertenece el usuario', related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='permisos de usuario', blank=True, help_text='Los permisos específicos concedidos a este usuario', related_name='customuser_permissions')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dni', 'fecha_nacimiento', 'email']

#Print del username
    def __str__(self):
        return self.username

    # class Meta:
    #     db_table = 'myapp_CustomUser'




