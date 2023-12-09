from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from .models import Producto, TipoRestaurante, TipoProducto, Restaurante, PedidoProducto
from django.contrib.auth import logout
from datetime import datetime

def index(request):
    return render(request, 'myapp/primera.html')

def listaRestaurantes(request, idTipoRestaurante):
    tipoRestaurante = get_object_or_404(TipoRestaurante, idTipoRestaurante=idTipoRestaurante)
    restaurantes = tipoRestaurante.restaurante_set.all()

    context = {
        'tipoRestaurante': tipoRestaurante,
        'restaurantes': restaurantes,
    }

    return render(request, 'restaurantes.html', context)

from django.shortcuts import render
from django.shortcuts import render

def restaurante(request, nombreRestaurante):
    restaurante = get_object_or_404(Restaurante, nombre=nombreRestaurante)
    productos = Producto.objects.filter(idRestaurante=restaurante)
    categorias = TipoProducto.objects.filter(producto__idRestaurante=restaurante).distinct()
    
    # Obtén el ID del restaurante
    restaurante_id = restaurante.idRestaurante

    # Obtener el nombre de usuario del usuario autenticado (si está autenticado)
    username = request.user.username if request.user.is_authenticated else None

    context = {
        'restaurante': restaurante,
        'productos': productos,
        'categorias': categorias,
        'username': username,  # Añadir el nombre de usuario al contexto
        'restaurante_id': restaurante_id,  # Añadir el ID del restaurante al contexto
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


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Pedido

from django.http import JsonResponse
import json

def guardar_pedido(request):
    if request.method == 'POST':
        # Retrieve the order data from the request
        importePedido = request.POST['importePedido']
        username = request.POST['username']
        id_restaurante = request.POST.get('id_restaurante')
        restaurante = Restaurante.objects.get(pk=id_restaurante)

        # Create a new Pedido instance
        pedido = Pedido()
        pedido.importePedido = importePedido
        pedido.username = User.objects.get(username=username)
        pedido.id_restaurante = restaurante
        pedido.save()

        # Retrieve product details from the request (as a JSON string)
        productos_json = request.POST.get('productos')

        # Convert the JSON string to a Python list of dictionaries
        productos = json.loads(productos_json)

        # Create ProductoPedido instances related to the order
        for producto in productos:
            producto_pedido = PedidoProducto()
            producto_pedido.idPedido = pedido
            producto_pedido.idProducto = Producto.objects.get(nombre=producto['titulo'])
            producto_pedido.cantidad = producto['cantidad']
            producto_pedido.save()

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Pedido guardado exitosamente'})

    # Handle GET requests or other HTTP methods
    return JsonResponse({'error': 'Método no permitido'}, status=405)

