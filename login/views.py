from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Vista de inicio de la página
    Retorna hacia la home.html
    """
    return render(request, 'login/home.html')


def products(request):
    return render(request, 'login/products.html')
