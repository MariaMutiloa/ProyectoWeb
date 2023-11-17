from django.urls import path
from .views import CustomLoginView, index
from .views import sushi_box, categoria, listaRestaurantes, sushi_artist, restaurantesSushi, kenji, fuji, verdeWok, sinfoniaVegana, jardinDeSabores, listaRamen, udon, shifu, yokohama, listaFusion, wok,sabor,este,cerrar


urlpatterns = [
    path('', index, name='index'),
    path('principal', categoria, name='principal'),
    path('login.html', CustomLoginView.as_view(), name='login'),
    path('sushi', restaurantesSushi, name='sushi'),
    path('SushiDonosti', sushi_box, name='SushiDonosti'),
    path('RestaurantesVegetarianos', listaRestaurantes, name='vegetariano'),
    path('SushiArtist', sushi_artist, name= 'Sushi Artist'),
    path('KenjiBar', kenji, name='Kenji Sushi Bar'),
    path('SushiFuji', fuji, name='Sushi Fuji'),
    path('VerdeWok', verdeWok, name ='VerdeWok'),
    path('SinfoniaVegana', sinfoniaVegana, name ='SinfoniaVegana'),
    path('JardinDeSabores', jardinDeSabores, name ='JardinDeSabores'),
    path('RestaurantesRamen', listaRamen, name='ramen'),
    path('Udon', udon, name ='Udon'),
    path('Shifu', shifu, name ='Shifu'),
    path('Yokohama', yokohama, name ='Yokohama'),
    path('RestaurantesFusion', listaFusion, name='fusion'),
    path('WokFusion', wok, name='WokFusion'),
    path('SaborOriental', sabor, name='SaborOriental'),
    path('EspeciasDelEste', este, name='EspeciasDelEste'),
    path('cerrar-sesion/', cerrar, name='cerrar')
]

