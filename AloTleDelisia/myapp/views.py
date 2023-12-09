from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from .models import Producto, TipoRestaurante, TipoProducto, Restaurante, PedidoProducto
from django.contrib.auth import logout
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Pedido
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'myapp/primera.html')

def listaRestaurantes(request, nombreTipo=None):
    tipoRestaurante = get_object_or_404(TipoRestaurante, nombre=nombreTipo) 
    restaurantes = tipoRestaurante.restaurante_set.all()

    context = {
        'tipoRestaurante': tipoRestaurante,
        'restaurantes': restaurantes,
    }

    return render(request, 'restaurantes.html', context)

def restaurante(request, nombreRestaurante):
    restaurante = get_object_or_404(Restaurante, nombre=nombreRestaurante)
    productos = Producto.objects.filter(idRestaurante=restaurante)
    categorias = TipoProducto.objects.filter(producto__idRestaurante=restaurante).distinct()

    restaurante_id = restaurante.idRestaurante

    username = request.user.username if request.user.is_authenticated else None

    context = {
        'restaurante': restaurante,
        'productos': productos,
        'categorias': categorias,
        'username': username, 
        'restaurante_id': restaurante_id,  
    }
    return render(request, 'unRestaurante.html', context)

class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'  

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('principal') 

def categoria(request):
    categorias = TipoRestaurante.objects.all()

    context = {'categorias': categorias}

    return render(request, 'myapp/principal.html', context)

def cerrar(request):
    logout(request)
    return redirect('index')

def guardar_pedido(request):
    if request.method == 'POST':
    
        importePedido = request.POST['importePedido']
        username = request.POST['username']
        id_restaurante = request.POST.get('id_restaurante')
        restaurante = Restaurante.objects.get(pk=id_restaurante)

        pedido = Pedido()
        pedido.importePedido = importePedido
        pedido.username = User.objects.get(username=username)
        pedido.id_restaurante = restaurante
        pedido.save()

      
        productos_json = request.POST.get('productos')

       
        productos = json.loads(productos_json)

       
        for producto in productos:
            producto_pedido = PedidoProducto()
            producto_pedido.idPedido = pedido
            producto_pedido.idProducto = Producto.objects.get(nombre=producto['titulo'])
            producto_pedido.cantidad = producto['cantidad']
            producto_pedido.save()

        return JsonResponse({'message': 'Pedido guardado exitosamente'})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

