from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """
    Vista de inicio de la página
    Retorna hacia la home.html
    """
    return render(request, 'login/home.html')

@login_required
def products(request):
    return render(request, 'login/products.html')
