from django.contrib import admin
from .models import User, Producto, Mensaje

# Register your models here.
admin.site.register(User)
admin.site.register(Producto)
admin.site.register(Mensaje)