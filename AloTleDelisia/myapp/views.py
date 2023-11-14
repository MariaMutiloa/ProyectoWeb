from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Producto

def index(request):
    return render(request, 'myapp/primera.html')

def login (request):
    return render (request,'myapp/login')


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'  # Ajusta a tu plantilla de inicio de sesión

    def form_valid(self, form):
        # Personaliza la lógica después de un inicio de sesión exitoso
        response = super().form_valid(form)

        # Redirige al usuario a la URL deseada después del inicio de sesión
        return redirect('principal')  # Ajusta 'home' a tu URL deseada



def principal(request):
    return render(request,'myapp/principal.html')


def sushi_box_view(request):
    productos = Producto.objects.filter(idTipoProducto=1, idRestaurante=1)

    context = {'productos': productos}

    return render(request, 'myapp/sushiDonosti.html', context)

def categoria(request):
    categoria = Producto.objects.filter(idTipoProducto=1, idRestaurante=1)

    context = {'productos': productos}

    return render(request, 'myapp/sushiDonosti.html', context)