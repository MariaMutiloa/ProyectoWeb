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
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.utils import translation

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


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('principal')  # Cambia 'principal' por la URL a la que quieres redirigir después del inicio de sesión
        else:
            # Manejar el caso en el que la autenticación falla, por ejemplo, mostrar un mensaje de error
            return render(request, 'myapp/login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'myapp/login.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro.html', {'form': form})

def categoria(request):
    categorias = TipoRestaurante.objects.all()

    context = {'categorias': categorias}

    return render(request, 'myapp/principal.html', context)

def usuario(request):
    return render(request, 'myapp/usuario.html')

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

def change_language(request):
    language = request.GET.get('language', 'es')  # 'en' es el idioma predeterminado

    # Cambia el idioma y actualiza la sesión
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language

    # Redirige a la página desde la que se hizo la solicitud
    return redirect(request.GET.get('next', '/'))