from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect   #redirige los datos a la pagina establecida (menos lineas de codigo)
from AppSuper.models import Producto, Mensaje   #importo mis models

#----IMPORTACIONES CARRITO Y TIENDA:---
from AppSuper.Carrito import Carrito
#----IMPORTACIONES LOGIN:----
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from AppSuper.forms import UserRegistrationForm, UserEditForm
#----IMPORTACIONES MENSAJES:--
from AppSuper.forms import MensajeFormulario
#----CARGA DE ARCHIVOS----
from django.core.files.storage import FileSystemStorage
from django.conf import settings


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

#--------CARGA ARCHIVOS----------

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'AppSuper/suba.html', {
            'uploaded_file_url': uploaded_file_url})
    return render(request, 'AppSuper/suba.html')
    
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

#----EDITAR USUARIO----
def editarPerfil(request):
    usuario = request.user #aca django manda directamente el modelo, no lo generamos nos

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, 'AppSuper/inicio.html',{'mensaje':f"Datos de {username} actualizados"})
    else:
        formulario = UserEditForm(initial={'email':usuario.email})
    return render(request, 'AppSuper/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})
 
#----CONTACTO----------
def mensajeFormulario(request):
    if request.method == 'POST':
        miFormulario = MensajeFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        texto = informacion['texto']
        mensaje = Mensaje(nombre=nombre, texto=texto)
        mensaje.save()
        return redirect("Tienda")
    else:
        miFormulario = MensajeFormulario()
    
    return render(request, 'AppSuper/mensajeFormulario.html', {'miFormulario':miFormulario})
