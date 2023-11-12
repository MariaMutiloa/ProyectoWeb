
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, index

urlpatterns = [
    path('', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('login.html/', CustomLoginView.as_view(), name='login'),
    path('home/', views.index, name='principal'),
]

