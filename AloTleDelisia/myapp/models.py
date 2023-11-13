from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    importePedido = models.DecimalField(max_digits=10, decimal_places=2)
    dia = models.DateField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    id_restaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE)


class TipoProducto(models.Model):
    idTipoProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion=models.TextField()


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcionProducto = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    idTipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    idRestaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE)


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

class Menu(models.Model):
    idMenu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    idTipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

class PedidoProducto(models.Model):
    idPedidoProducto = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class ProductoMenu(models.Model):
    idProductoMenu = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idMenu = models.ForeignKey(Menu, on_delete=models.CASCADE)





