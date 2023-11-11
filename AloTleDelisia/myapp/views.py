from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Usuario


def index(request):
    return render(request, 'myapp/primera.html')

def login (request):
    return render (request,'myapp/login.html')

def verificarUsuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            try:
                usuario_bd = Usuario.objects.get(correo=correo)
                print(f"Usuario encontrado: {usuario_bd}")
            except Usuario.DoesNotExist:
                print(f"Usuario no encontrado para el correo: {correo}")
                return render(request, 'myapp/login.html', {'error_message': 'Correo electrónico o contraseña incorrectos'})

            print(f"Contraseña almacenada: {usuario_bd.password}")

            user = authenticate(request, username=correo, password=password)

            if user is not None:
                login(request, user)
                print("Inicio de sesión exitoso")
                return redirect('principal')
            else:
                print(f"Error de autenticación: {user}")
                return render(request, 'myapp/login.html', {'error_message': 'Correo electrónico o contraseña incorrectos'})
    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})



def principal(request):
    return render(request, 'myapp/principal.html')