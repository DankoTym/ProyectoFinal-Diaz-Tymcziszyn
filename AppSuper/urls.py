from django.urls import path
from AppSuper import views
from AppSuper.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
from django.contrib.auth.views import LogoutView    #Esto es solo para el logout


urlpatterns = [
    #path('', views.Inicio, name="inicio"),
    path('', tienda, name="Tienda"),
    #ACIONES DEL CARRITO:
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    #USER:
    path('login/', views.login_request, name="login"),
    path('registro/', views.register_request, name="registro"),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
    path('loguot', LogoutView.as_view(template_name='AppSuper/logout.html'), name="logout"),
    #Mensaje:
    path('mensajeFormulario/', views.mensajeFormulario, name="mensajeFormulario"),
    #carga archivo:
    path('suba', views.simple_upload, name='suba')
]

