from django.contrib import admin
from django.urls import path, include
from .views import ingresarProd,anadirProd, Carrito, Comprar, HistorialCompras, Invetario, MenuP, ModificarContra, Producto1, Producto2, Producto3, Producto4, RecuperarContra, RegistroUsuario, Ventas

urlpatterns = [
    path('anadirProd',anadirProd,name="anadirProd"),
    path('Carrito',Carrito,name="Carrito"),
    path('Comprar',Comprar,name="Comprar"),
    path('HistorialCompras',HistorialCompras,name="HistorialCompras"),
    path('Invetario',Invetario,name="Invetario"),
    path('',MenuP,name="MenuP"),
    path('ModificarContra',ModificarContra,name="ModificarContra"),
    path('Producto1',Producto1,name="Producto1"),
    path('Producto2',Producto2,name="Producto2"),
    path('Producto3',Producto3,name="Producto3"),
    path('Producto4',Producto4,name="Producto4"),
    path('RecuperarContra',RecuperarContra,name="RecuperarContra"),
    path('RegistroUsuario',RegistroUsuario,name="RegistroUsuario"),
    path('Ventas',Ventas,name="Ventas"),
    path('ingresarProd',ingresarProd,name:"ingresarProd")
]