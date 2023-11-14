from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Producto, TipoRestaurante

def index(request):
    return render(request, 'myapp/primera.html')

def login (request):
    return render (request,'myapp/login')


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'  

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('principal')  


def sushi_box(request):
    productosTipo1 = Producto.objects.filter(idRestaurante=1, idTipoProducto=1)
    productosTipo2 = Producto.objects.filter(idRestaurante=1, idTipoProducto=2)
    productosTipo3 = Producto.objects.filter(idRestaurante=1, idTipoProducto=3)
    context = {
        'productosTipo1': productosTipo1,
        'productosTipo2': productosTipo2,
        'productosTipo3': productosTipo3
    }
    return render(request, 'myapp/sushiDonosti.html', context)


def categoria(request):
    categorias = TipoRestaurante.objects.all()

    context = {'categorias': categorias}

    return render(request, 'myapp/principal.html', context)