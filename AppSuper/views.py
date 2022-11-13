from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from AppSuper.Carrito import Carrito
from AppSuper.models import Producto

# Create your views here.
#----Carrito de Compras:------
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "AppSuper/tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    productos = Producto.objects.all()
    return render(request, "AppSuper/tienda.html", {'productos':productos, 'carrito':carrito})


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    productos = Producto.objects.all()
    return render(request, "AppSuper/tienda.html", {'productos':productos, 'carrito':carrito})

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    productos = Producto.objects.all()
    return render(request, "AppSuper/tienda.html", {'productos':productos, 'carrito':carrito})

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    productos = Producto.objects.all()
    return render(request, "AppSuper/tienda.html", {'productos':productos, 'carrito':carrito})

#-----------------------------