from django.db import models
from django.conf import settings

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

class PedidoProducto(models.Model):
    idPedidoProducto = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()


