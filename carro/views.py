from django.shortcuts import render, redirect
from carro.carro import Carro
from tienda.models import Productos

# Create your views here.

def agregar_a_carro(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.add_product(producto)
    return redirect('/tienda/')

def delete_product(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.delete_product(producto)
    return redirect('/tienda/')

def restar(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar_unidades(producto)
    return redirect('/tienda/')

def limpiar_carro(request):
    carro = Carro(request)
    carro.delete_all()
    return redirect('/tienda/')
