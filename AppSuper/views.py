from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#----IMPORTACIONES CARRITO Y TIENDA:---
from AppSuper.Carrito import Carrito
from AppSuper.models import Producto
from django.shortcuts import redirect   #redirige los datos a la pagina establecida (menos lineas de codigo)
#----IMPORTACIONES LOGIN:----
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from AppSuper.forms import UserRegistrationForm, UserEditForm


#----Carrito de Compras:------
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "AppSuper/tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")
 

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

#----------LOGIN---------------
#------INGRESAR-----
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(render, request.POST)

        if form.is_valid():
            
            usuario = request.POST.get('username')
            clave = request.POST.get('password')
            user = authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)    #si existe usuario, lo loguea
                return render(request, 'AppSuper/inicio.html', {'mensaje':f'Bienvenido {usuario}'})    
            else:
                return render(request, 'AppSuper/inicio.html', {'mensaje':'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'AppSuper/inicio.html', {'mensaje':'Error, Formulario Erroneo'})
    else:
        form = AuthenticationForm()
        return render(request, 'AppSuper/login.html', {'form':form})
#---Crear usuario-----
def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'AppSuper/inicio.html', {'mensaje':f"Usuario {username} creado"})
        else:
            return render(request, 'AppSuper/inicio.html', {'mensaje':"No se pudeo crear el usuario"})
    else:
        form = UserRegistrationForm()
        return render(request, 'AppSuper/tienda.html', {'form':form})