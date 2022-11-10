from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contacto = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre+" "+ self.apellido+" - Contacto: "+str(self.contacto)

class Articulo(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.nombre+" - Precio: "+str(self.precio)

class Mensaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.usuario.nombre+ " " +str(self.usuario.apellido)
    



#class Avatar(models.Model):
#   articulo = models.ForeignKey (Articulo, on_delete=models.CASCADE)

