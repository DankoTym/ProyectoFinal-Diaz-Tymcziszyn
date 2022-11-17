
from django.contrib import admin
from django.urls import path, include
from django.conf import settings    #importo los archivos de settins para que mis url apunten a mi directorio fisico
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppSuper/', include('AppSuper.urls')) #conecto mi app con el url principal
]

if settings. DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #esto es para proyecto en desarrollo, hace que la imagen se busque en el directorio fisico de nuestra PC
