from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Producto, TipoRestaurante, TipoProducto, Restaurante
from django.contrib.auth import logout
from django.urls import reverse

def index(request):
    return render(request, 'myapp/primera.html')

def login (request):
    return render (request,'myapp/login')


def verdeWok (request):
    return render(request, 'myapp/verdeWok.html')

def sinfoniaVegana (request):
    return render(request, 'myapp/sinfoniaVegana.html')

def jardinDeSabores (request):
    return render(request, 'myapp/jardinDeSabores.html')


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'  

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('principal')  


def listaRestaurantes(request):
    restauranteTipo1 = Restaurante.objects.filter(idTipoRestaurante=2)
    context = {
        'restaurantes': restauranteTipo1,
    }
    return render(request, 'myapp/tipoVegetariano.html', context)

def restaurantesSushi(request):
    restauranteTipo1= Restaurante.objects.filter(idTipoRestaurante=1)
    context = {
            'restaurantes': restauranteTipo1,
        }
    return render(request, 'myapp/tipoSushi.html', context)

def listaRamen(request):
    restauranteTipo1 = Restaurante.objects.filter(idTipoRestaurante=3)
    context = {
        'restaurantes': restauranteTipo1,
    }
    return render(request, 'myapp/tipoRamen.html', context)

def listaFusion(request):
    restauranteTipo1 = Restaurante.objects.filter(idTipoRestaurante=4)
    context = {
        'restaurantes': restauranteTipo1,
    }
    return render(request, 'myapp/tipoFusion.html', context)

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

def kenji(request):
    productosTipo1 = Producto.objects.filter(idRestaurante=6, idTipoProducto=12)
    productosTipo2 = Producto.objects.filter(idRestaurante=6, idTipoProducto=13)
    productosTipo3 = Producto.objects.filter(idRestaurante=6, idTipoProducto=14)
    productosTipo4 = Producto.objects.filter(idRestaurante=6, idTipoProducto=15)
    categorias=TipoProducto.objects.filter(idRestaurante=6)
    context = {
        'productosTipo1': productosTipo1,
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3,
        'productosTipo4': productosTipo4,
        'categorias': categorias
    }
    return render(request, 'myapp/kenjiSushi.html', context)

def fuji(request):
    productosTipo1 = Producto.objects.filter(idRestaurante=7, idTipoProducto=16)
    productosTipo2 = Producto.objects.filter(idRestaurante=7, idTipoProducto=17)
    productosTipo3 = Producto.objects.filter(idRestaurante=7, idTipoProducto=18)
    productosTipo4 = Producto.objects.filter(idRestaurante=7, idTipoProducto=19)
    productosTipo5 = Producto.objects.filter(idRestaurante=7, idTipoProducto=20)
    productosTipo6 = Producto.objects.filter(idRestaurante=7, idTipoProducto=21)
    categorias=TipoProducto.objects.filter(idRestaurante=7)
    context = {
        'productosTipo1': productosTipo1,
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3,
        'productosTipo4': productosTipo4,
        'productosTipo5': productosTipo5,
        'productosTipo6': productosTipo6,
        'categorias': categorias
    }
    return render(request, 'myapp/sushiFuji.html', context)

def udon (request):
    productosTipo1 = Producto.objects.filter(idRestaurante=8, idTipoProducto=22)
    productosTipo2 = Producto.objects.filter(idRestaurante=8, idTipoProducto=23)
    productosTipo3 = Producto.objects.filter(idRestaurante=8, idTipoProducto=24)
    productosTipo4 = Producto.objects.filter(idRestaurante=8, idTipoProducto=25)
    categorias=TipoProducto.objects.filter(idRestaurante=8)
    context = {
        'productosTipo1': productosTipo1,
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3,
        'productosTipo4': productosTipo4,
        'categorias': categorias
    }
    return render(request, 'myapp/udon.html', context)

def shifu (request):
    productosTipo1 = Producto.objects.filter(idRestaurante=9, idTipoProducto=26)
    productosTipo2 = Producto.objects.filter(idRestaurante=9, idTipoProducto=27)
    productosTipo3 = Producto.objects.filter(idRestaurante=9, idTipoProducto=28)
    productosTipo4 = Producto.objects.filter(idRestaurante=9, idTipoProducto=29)
    productosTipo5 = Producto.objects.filter(idRestaurante=9, idTipoProducto=30)
    categorias=TipoProducto.objects.filter(idRestaurante=9)
    context = {
        'productosTipo1': productosTipo1,
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3,
        'productosTipo4': productosTipo4,
        'productosTipo5': productosTipo5,
        'categorias': categorias
    }
    return render(request, 'myapp/ramenShifu.html', context)

def yokohama (request):
    productosTipo2 = Producto.objects.filter(idRestaurante=10, idTipoProducto=32)
    productosTipo3 = Producto.objects.filter(idRestaurante=10, idTipoProducto=33)
    productosTipo4 = Producto.objects.filter(idRestaurante=10, idTipoProducto=34)
    productosTipo5 = Producto.objects.filter(idRestaurante=10, idTipoProducto=35)
    categorias=TipoProducto.objects.filter(idRestaurante=10)
    context = {
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3,
        'productosTipo4': productosTipo4,
        'productosTipo5': productosTipo5,
        'categorias': categorias
    }
    return render(request, 'myapp/yokohama.html', context)


def categoria(request):
    categorias = TipoRestaurante.objects.all()

    context = {'categorias': categorias}

    return render(request, 'myapp/principal.html', context)

def cerrar(request):
    logout(request)
    return redirect(reverse('index'))
