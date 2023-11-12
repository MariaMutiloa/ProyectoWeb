from django.urls import path
from .views import CustomLoginView, index, principal

urlpatterns = [
    path('', index, name='index'),
    path('principal/', principal, name='principal'),
    path('login.html/', CustomLoginView.as_view(), name='login'),
]

