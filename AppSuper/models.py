from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombre,apellido,password = None):
        if not email:
            raise ValueError('Debe tener un EMAIL')
        
        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido)
        usuario.set_password(password)         #Esto es para no pasar la contraseña como texto plano (darle un poco más de encriptación)
        usuario.save()
        return usuario
    
    def create_superuser(self,username,email,nombre,apellido,password):
        usuario = self.create_user(
            email=email,
            username=username,
            nombre=nombre,
            apellido=apellido,
            password=password)
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre usuario', unique=True, max_length=30)
    email = models.EmailField('Email', max_length=30, unique=True)
    nombre = models.CharField('Nombre', max_length=30, blank=True, null=True)
    apellido = models.CharField('Apellido', max_length=30, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=True)
    object = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    
    def has_perm(self,perm,ob = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

#---------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True) #sube la imagen a una carpeta "productos" en "media"

    def __str__(self):
        return f'{self.nombre} -> ${self.precio}'
#---------------------------------
class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    texto = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.nombre
 #--------------------------------  