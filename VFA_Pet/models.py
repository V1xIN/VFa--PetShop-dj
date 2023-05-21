from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(primary_key=True,verbose_name='Rut del usuario')
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    fono = models.IntegerField(max_length=15)
    clave = models.CharField(max_length=15)
    

class Venta(models.MODEL):
    codVenta = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
