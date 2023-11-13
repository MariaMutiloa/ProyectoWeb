from django.urls import path
from .views import CustomLoginView, index, principal
from .views import sushi_box_view


urlpatterns = [
    path('', index, name='index'),
    path('principal/', principal, name='principal'),
    path('login.html/', CustomLoginView.as_view(), name='login'),
    path('SushiDonosti/', sushi_box_view, name='SushiDonosti'),
]

