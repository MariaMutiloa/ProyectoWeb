from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, 'myapp/primera.html')

class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'  # Ajusta a tu plantilla de inicio de sesión

    def form_valid(self, form):
        # Personaliza la lógica después de un inicio de sesión exitoso
        response = super().form_valid(form)

        # Redirige al usuario a la URL deseada después del inicio de sesión
        return redirect('principal')  # Ajusta 'home' a tu URL deseada


def principal(request):
    return render(request, 'myapp/principal.html')