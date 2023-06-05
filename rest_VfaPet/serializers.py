from rest_framework import serializers
from VFA_Pet.models import Usuario,Venta

class Usuarioserializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['rut','nombre','apellido','correo','fono','clave','rol','pregunta','respuesta']


class Ventaserializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ["codVenta","usuario","fVenta","fEntrega","estadoP","direccion","total","carrito","status"]
