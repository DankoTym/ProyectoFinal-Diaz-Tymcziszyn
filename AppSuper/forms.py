from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


#Esto sirve para que en el .html se reflejen los datos que necesito
#Este block es para el registro de usuario 
#------REGISTRO----------
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
class Meta:
    models = User   #Esta info la genera Django internamente
    fields = {'username', 'email', 'password1', 'password2'}

    help_text = {k:"" for k in fields}

#----------Edición de User---------- 
class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
class Meta:
    model = User    #Esta info la genera Django internamente
    fields = {'email', 'password1', 'password2'}
    help_text = {k:"" for k in fields}

#---Mensajes:----
class MensajeFormulario(forms.Form):            
    nombre = forms.CharField(max_length=50)
    texto = forms.CharField(max_length=150)

#----Carga imagenes2----

class StudentForm(forms.Form):
    firstname = forms.CharField(label="Nombre", max_length=50)
    lastname = forms.CharField(label="Apellido", max_length=50)
    email = forms.EmailField(label="Correo")
    time = forms.DateField(label="Fecha subida")
    file = forms.FileField(label="Archivo")

#----Para ordenamiento de vista de la tienda----

class ListaProductos(forms.Form):
    product = forms.CharField(label="Producto", max_length=50)


