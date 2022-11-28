from django.contrib import admin
from .models import Producto, Mensaje, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Mensaje)