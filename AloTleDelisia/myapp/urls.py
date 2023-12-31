from django.urls import path
from .views import index
from .views import categoria, listaRestaurantes,cerrar,restaurante,guardar_pedido,login,register_view,pedidoUsuario
from django.views.i18n import set_language

urlpatterns = [
    path('', index, name='index'),
    path('principal', categoria, name='principal'),
    path('login/', login, name='login'),
    path('cerrar-sesion/', cerrar, name='cerrar'),
    path('restaurantes/', listaRestaurantes, name='restaurantes'),
    path('restaurantes/<str:idTipoRestaurante>', listaRestaurantes, name='listaRestaurantes'),
    path('restaurante/', restaurante, name='unRestaurante'),
    path('restaurante/<str:nombreRestaurante>', restaurante, name='restaurante'),
    path('pedidos/guardar', guardar_pedido, name='guardar_pedido'),
    path('registro/',register_view , name='registro'),
    path('set_language/', set_language, name='set_language'),
    path('miPerfil/', pedidoUsuario, name='usuario')
]

