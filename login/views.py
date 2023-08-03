from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def home(request):
    """
    Vista de inicio de la página
    Retorna hacia la home.html
    """
    return render(request, 'login/home.html')

@login_required
def products(request):
    """
    Vista recibe request
    Retorna la plantilla de productos
    """
    return render(request, 'login/products.html')

def exit(request):
    """
    Vista recibe request
    Retorna redirección hacia home
    """
    logout(request)
    return redirect('home')
