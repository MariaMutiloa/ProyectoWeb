from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, TipoRestaurante, TipoProducto, Restaurante, PedidoProducto, Pedido
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login
from django.utils import translation
from .forms import SignUpForm


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

def pedidoUsuario(request):
    usuario = request.user
    pedidosUsuario = Pedido.objects.filter(username=usuario)
    productosPedido = PedidoProducto.objects.filter(idPedido__in=pedidosUsuario)

    context = {
        'usuario': usuario,
        'pedidos': pedidosUsuario,
        'productosPedido': productosPedido,
    }
    return render(request, 'myapp/usuario.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('principal') 
        else:
            return render(request, 'myapp/login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'myapp/login.html')


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registro.html', {'form': form})

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
        idRestaurante = request.POST.get('idRestaurante')
        restaurante = Restaurante.objects.get(pk=idRestaurante)

        pedido = Pedido()
        pedido.importePedido = importePedido
        pedido.username = User.objects.get(username=username)
        pedido.idRestaurante = restaurante
        pedido.save()

      
        productos_json = request.POST.get('productos')

       
        productos = json.loads(productos_json)

       
        for producto in productos:
            productoPedido = PedidoProducto()
            productoPedido.idPedido = pedido
            productoPedido.idProducto = Producto.objects.get(nombre=producto['titulo'])
            productoPedido.cantidad = producto['cantidad']
            productoPedido.save()

        return JsonResponse({'message': 'Pedido guardado exitosamente'})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def change_language(request):
    language = request.GET.get('language', 'es')  # 'en' es el idioma predeterminado

    # Cambia el idioma y actualiza la sesión
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language

    # Redirige a la página desde la que se hizo la solicitud
    return redirect(request.GET.get('next', '/'))
