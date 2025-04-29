from django.shortcuts import render
from tienda.models import Productos

# Create your views here.

def tienda(request):
    productos = Productos.objects.all()
    return render(request, 'tienda/tienda.html', {'productos':productos})
