from django.contrib import admin
from django.urls import path, include
from .views import detalle_Venta,detalle_usuario,lista_Usuario,lista_Venta
from .viewslogin import login
urlpatterns = [
    path('lista_Usuario',lista_Usuario,name="lista_Usuario"),
    path('lista_Venta',lista_Venta,name="lista_Venta"),
    path('detalle_usuario/<rut>',detalle_usuario,name="detalle_usuario"),
    path('detalle_Venta/<codVenta>',detalle_Venta,name="detalle_Venta"),
    path('login', login, name="login"),
]