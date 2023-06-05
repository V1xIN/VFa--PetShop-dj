from django.contrib import admin
from django.urls import path, include
from .views import lista_Usuario,lista_Venta
urlpatterns = [
    path('lista_Usuario',lista_Usuario,name="lista_Usuario"),
    path('lista_Venta',lista_Venta,name="lista_Venta"),

]