from django.urls import path
from .views import CustomLoginView, index
from .views import sushi_box, categoria


urlpatterns = [
    path('', index, name='index'),
    path('principal', categoria, name='principal'),
    path('login.html', CustomLoginView.as_view(), name='login'),
    path('SushiDonosti', sushi_box, name='SushiDonosti'),
]

