from django.urls import path
from .views import index
from .views import categoria, listaRestaurantes,cerrar,restaurante,guardar_pedido,login,register_view,pedidoUsuario
from django.views.i18n import set_language
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', index, name='index'),
    path(_('principal'), categoria, name='principal'),
    path('login/', login, name='login'),
    path(_('cerrar-sesion/'), cerrar, name='cerrar'),
    path(_('restaurantes/'), listaRestaurantes, name='restaurantes'),
    path('restaurantes/<str:idTipoRestaurante>', listaRestaurantes, name='listaRestaurantes'),
    path(_('restaurante/'), restaurante, name='unRestaurante'),
    path('restaurante/<str:nombreRestaurante>', restaurante, name='restaurante'),
    path(_('pedidos/guardar'), guardar_pedido, name='guardar_pedido'),
    path(_('registro/'),register_view , name='registro'),
    path('set_language/', set_language, name='set_language'),
    path(_('miPerfil/'), pedidoUsuario, name='usuario')
]

