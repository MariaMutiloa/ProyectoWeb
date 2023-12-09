from django.urls import path
from .views import index
from .views import categoria, listaRestaurantes,cerrar,restaurante,guardar_pedido,login


urlpatterns = [
    path('', index, name='index'),
    path('principal', categoria, name='principal'),
    path('login/', login, name='login'),
    path('cerrar-sesion/', cerrar, name='cerrar'),
    path('restaurantes/', listaRestaurantes, name='restaurantes'),
    path('restaurantes/<str:idTipoRestaurante>', listaRestaurantes, name='listaRestaurantes'),
    path('restaurante/', restaurante, name='unRestaurante'),
    path('restaurante/<str:nombreRestaurante>', restaurante, name='restaurante'),
    path('pedidos/guardar', guardar_pedido, name='guardar_pedido')
]

