from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contacto = models.CharField(max_length=30)
    #imagen = models.ImageField(upload_to="usuario", null=True)

    def __str__(self) -> str:
        return self.nombre+" "+ self.apellido+" - Contacto: "+str(self.contacto)

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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.usuario.nombre+ " " +str(self.usuario.apellido)
 #--------------------------------  


