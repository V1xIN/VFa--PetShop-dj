from django.db import models

# Create your models here.

class Rol(models.Model):
    idRol = models.IntegerField(primary_key=True max_length=2)
    nombreRol = models.CharField(max_length=20)

class Pregunta(models.Model):
    idPregunta = models.IntegerField(primary_key=True max_length=2)
    descripcion = models.CharField(max_length=20)

class Usuario(models.Model):
    rut = models.CharField(primary_key=True,verbose_name='Rut del usuario')
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    fono = models.IntegerField(max_length=15)
    clave = models.CharField(max_length=15)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=20)

class Region(models.Model):
    idRegion =models.AutoField(primary_key=True)
    nombreR = models.CharField(max_length=20)

class Comuna(models.Model):
    idComuna =models.AutoField(primary_key=True)
    nombreC = models.CharField(max_length=20)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

class Direccion(models.Model):
    idDireccion =models.AutoField(primary_key=True)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    calle = models.CharField(max_length=20)
    numero = models.IntegerField(max_length=20)
    casa = models.BooleanField()
    dpto = models.BooleanField()
    piso = models.IntegerField(10)

class Venta(models.Model):
    codVenta = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fVenta = models.DateField(verbose_name='Fecha de la venta')
    fEntrega = models.DateField(verbose_name='Fecha de la entrega')
    estadoP = models.BooleanField(verbose_name='estado del producto')
    idDireccion = models.AutoField()
    total = models.IntegerField(max_length=10)
    carrito = models.BooleanField()
    status = models.BooleanField()

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCa = models.CharField(max_length=20)

class Producto(models.Model):
    codProducto = models.AutoField(primary_key=True)
    nombreP = models.CharField(max_length=20)
    stock = models.IntegerField(max_length=10)
    descipcion = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="VFA_PetShop")
    precio = models.IntegerField(max_length=15)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

class DetalleVenta(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(max_length=5)
    subtotal = models.IntegerField(15)
