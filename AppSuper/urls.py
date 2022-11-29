from django.urls import path
from AppSuper import views
from AppSuper.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito 
from django.contrib.auth.views import LogoutView    #Esto es solo para el logout
from django.contrib import admin



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
    path('suba/',views.index),
    
    path('Producto/lista/', views.ProductoList.as_view(), name="Producto_list"),
    path('Producto/<pk>', views.ProductoDitail.as_view(), name="Producto_detalle"),        #el <pk> pasa de forma automatica el id por django
    path('Producto/nuevo/', views.ProductoCrear.as_view(), name="Producto_crear"),
    path('Producto/edit/<pk>', views.ProductoEdicion.as_view(), name="Producto_editar"),
    path('Producto/delete/<pk>', views.ProductoEliminacion.as_view(), name="Producto_eliminar"),

    path('about/', views.about, name="about"),

    path('Mensaje/lista/', views.MensajeList.as_view(), name="Mensaje_list"),
    path('Mensaje/<pk>', views.MensajeDitail.as_view(), name="Mensaje_detalle"),
    path('Mensaje/delete/<pk>', views.MensajeEliminacion.as_view(), name="Mensaje_eliminar"),
]

