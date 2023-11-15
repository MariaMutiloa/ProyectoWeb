from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Producto, TipoRestaurante, Restaurante

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
    # restauranteTipo2 = TipoRestaurante.objects.filter(idTipoRestaurante=2)
    # restauranteTipo3 = TipoRestaurante.objects.filter(idTipoRestaurante=2)
    # restauranteTipo4 = TipoRestaurante.objects.filter(idTipoRestaurante=2)
    # restauranteTipo5 = TipoRestaurante.objects.filter(idTipoRestaurante=2)
    context = {
        'restaurante': restauranteTipo1,
        # 'restauranteTipo2': restauranteTipo2,
        # 'restauranteTipo3': restauranteTipo3,
        # 'restauranteTipo4': restauranteTipo4,
        # 'restauranteTipo5': restauranteTipo5
    }
    return render(request, 'myapp/tipoVegetariano.html', context)

# def restaurante(request):
#     restaurantes = idTipoRestaurante.objects.all()

#     context = {'restaurantes': restaurantes}

#     return render(request, 'myapp/principal.html', context)


def sushi_box(request):
    productosTipo1 = Producto.objects.filter(idRestaurante=1, idTipoProducto=1)
    productosTipo2 = Producto.objects.filter(idRestaurante=1, idTipoProducto=2)
    productosTipo3 = Producto.objects.filter(idRestaurante=1, idTipoProducto=3)
    productosTipo4 = Producto.objects.filter(idRestaurante=1, idTipoProducto=4)
    productosTipo5 = Producto.objects.filter(idRestaurante=1, idTipoProducto=5)
    context = {
        'productosTipo1': productosTipo1,
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3,
        'productosTipo4': productosTipo4,
        'productosTipo5': productosTipo5
    }
    return render(request, 'myapp/sushiDonosti.html', context)


def categoria(request):
    categorias = TipoRestaurante.objects.all()

    context = {'categorias': categorias}

    return render(request, 'myapp/principal.html', context)