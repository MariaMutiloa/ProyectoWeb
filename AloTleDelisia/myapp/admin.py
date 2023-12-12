from django.contrib import admin
from .models import Pedido, TipoProducto, Producto, TipoRestaurante, Restaurante, PedidoProducto

# Register your models here.
admin.site.register(Pedido)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(TipoRestaurante)
admin.site.register(Restaurante)
admin.site.register(PedidoProducto)


