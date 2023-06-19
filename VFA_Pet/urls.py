from django.contrib import admin
from django.urls import path, include
from .views import iniciar_sesion,actualizarProducto,eliminarProd,ingresarUser,ingresarProd,anadirProd, Carrito, Comprar, HistorialCompras, Inventario, MenuP, ModificarContra, Producto1, Producto2, Producto3, Producto4, RecuperarContra, RegistroUsuario, Ventas, ModificarProd

urlpatterns = [
    path('MenuP',MenuP,name="MenuP"),
    path('',Comprar,name="Comprar"),
    path('iniciar_sesion',iniciar_sesion,name="iniciar_sesion"),
    path('anadirProd',anadirProd,name="anadirProd"),
    path('Carrito',Carrito,name="Carrito"),
    path('HistorialCompras',HistorialCompras,name="HistorialCompras"),
    path('Inventario',Inventario,name="Inventario"),
    path('ModificarContra',ModificarContra,name="ModificarContra"),
    path('Producto1/<int:codigo>',Producto1,name="Producto1"),
    path('RecuperarContra',RecuperarContra,name="RecuperarContra"),
    path('RegistroUsuario',RegistroUsuario,name="RegistroUsuario"),
    path('Ventas',Ventas,name="Ventas"),
    path('ingresarProd',ingresarProd,name="ingresarProd"),
    path('ingresarUser',ingresarUser,name="ingresarUser"),
    path('eliminarProd/<int:codProd>',eliminarProd,name="eliminarProd"),
    path('ModificarProd/<int:codProd>',ModificarProd,name="ModificarProd"),
    path('actualizarProducto',actualizarProducto,name="actualizarProducto"),
    
]