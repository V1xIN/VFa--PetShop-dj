from django.contrib import admin
from .models import Rol,Pregunta,Usuario,Region,Comuna,Direccion,Venta,Categoria,Producto,DetalleVenta
# Register your models here.

admin.site.register(Rol)
admin.site.register(Pregunta)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Venta)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(DetalleVenta)