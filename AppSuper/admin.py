from django.contrib import admin
from .models import User, Articulo, Mensaje

# Register your models here.
admin.site.register(User)
admin.site.register(Articulo)
admin.site.register(Mensaje)