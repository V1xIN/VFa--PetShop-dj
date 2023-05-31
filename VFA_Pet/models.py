from django.db import models

# Create your models here.

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombreRol = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreRol

class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key=True )
    descripcion = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.descripcion

class Usuario(models.Model):
    rut = models.CharField(primary_key=True,max_length=12, verbose_name='Rut del usuario')
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=40)
    fono = models.IntegerField()
    clave = models.CharField(max_length=15)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre
    
class Region(models.Model):
    idRegion =models.AutoField(primary_key=True)
    nombreR = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreR

class Comuna(models.Model):
    idComuna =models.AutoField(primary_key=True)
    nombreC = models.CharField(max_length=20)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreC

class Direccion(models.Model):
    idDireccion =models.AutoField(primary_key=True)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()
    casa = models.IntegerField()
    dpto = models.IntegerField()
    piso = models.IntegerField(10)

    def __str__(self) -> str:
        return self.calle
    
class Venta(models.Model):
    codVenta = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fVenta = models.DateField(verbose_name='Fecha de la venta')
    fEntrega = models.DateField(verbose_name='Fecha de la entrega')
    estadoP = models.IntegerField(verbose_name='estado del producto')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    total = models.IntegerField()
    carrito = models.IntegerField()
    status = models.IntegerField()

    
    
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCa = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreCa

class Producto(models.Model):
    codProducto = models.AutoField(primary_key=True)
    nombreP = models.CharField(max_length=20)
    stock = models.IntegerField()
    descipcion = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="VFA_PetShop")
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreP
    
class DetalleVenta(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

