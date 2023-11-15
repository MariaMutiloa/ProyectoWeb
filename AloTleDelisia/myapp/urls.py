from django.urls import path
from .views import CustomLoginView, index
from .views import sushi_box, categoria, listaRestaurantes, sushi_artist


urlpatterns = [
    path('', index, name='index'),
    path('principal', categoria, name='principal'),
    path('login.html', CustomLoginView.as_view(), name='login'),
    path('SushiDonosti', sushi_box, name='SushiDonosti'),
    path('RestaurantesVegetarianos', listaRestaurantes, name='vegetariano'),
    path('SushiArtist', sushi_artist, name= 'SushiArtist')
]

