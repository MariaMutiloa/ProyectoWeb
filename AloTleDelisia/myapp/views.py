from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Producto, TipoRestaurante, TipoProducto, Restaurante

def index(request):
    return render(request, 'myapp/primera.html')

def login (request):
    return render (request,'myapp/login')


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'  

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('principal')  


def listaRestaurantes(request):
    restauranteTipo1 = Restaurante.objects.filter(idTipoRestaurante=2)
    context = {
        'restaurante': restauranteTipo1,
    }
    return render(request, 'myapp/tipoVegetariano.html', context)

def restaurantesSushi(request):
    restauranteTipo1= Restaurante.objects.filter(idTipoRestaurante=1)
    context = {
            'restaurantes': restauranteTipo1,
        }
    return render(request, 'myapp/tipoSushi.html', context)

def sushi_box(request):
    productosTipo1 = Producto.objects.filter(idRestaurante=1, idTipoProducto=1)
    productosTipo2 = Producto.objects.filter(idRestaurante=1, idTipoProducto=2)
    productosTipo3 = Producto.objects.filter(idRestaurante=1, idTipoProducto=3)
    productosTipo4 = Producto.objects.filter(idRestaurante=1, idTipoProducto=4)
    productosTipo5 = Producto.objects.filter(idRestaurante=1, idTipoProducto=5)
    categorias=TipoProducto.objects.filter(idRestaurante=1)
    context = {
        'productosTipo1': productosTipo1,
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3,
        'productosTipo4': productosTipo4,
        'productosTipo5': productosTipo5,
        'categorias': categorias
    }
    return render(request, 'myapp/sushiDonosti.html', context)


def sushi_artist(request):
    productosTipo1 = Producto.objects.filter(idRestaurante=2, idTipoProducto=6)
    productosTipo2 = Producto.objects.filter(idRestaurante=2, idTipoProducto=7)
    productosTipo3 = Producto.objects.filter(idRestaurante=2, idTipoProducto=8)
    productosTipo4 = Producto.objects.filter(idRestaurante=2, idTipoProducto=9)
    productosTipo5 = Producto.objects.filter(idRestaurante=2, idTipoProducto=10)
    productosTipo6 = Producto.objects.filter(idRestaurante=2, idTipoProducto=11)
    categorias=TipoProducto.objects.filter(idRestaurante=2)
    context = {
        'productosTipo1': productosTipo1,
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3,
        'productosTipo4': productosTipo4,
        'productosTipo5': productosTipo5,
        'categorias': categorias
    }
    return render(request, 'myapp/sushiArtist.html', context)


def categoria(request):
    categorias = TipoRestaurante.objects.all()

    context = {'categorias': categorias}

    return render(request, 'myapp/principal.html', context)