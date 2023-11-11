
from .views import verificarUsuario
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verificar-usuario/', views.verificarUsuario, name='verificarUsuario'),
    path('principal/', views.principal, name='principal'),
     path('login.html/', views.login, name='login') 
]

