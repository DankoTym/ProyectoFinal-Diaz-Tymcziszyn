from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

#---------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True) #sube la imagen a una carpeta "productos" 


    def __str__(self):
        return f'{self.nombre} -> ${self.precio}'
#---------------------------------
class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    texto = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.nombre
 #--------------------------------  