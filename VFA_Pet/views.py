from django.shortcuts import render, redirect
from .models import Producto,Categoria,Usuario,Rol,Pregunta,Venta
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# Create your views here.

def anadirProd(request):
    arreglocat = Categoria.objects.all()
    contexto ={
        "categoria": arreglocat

    }
    return render(request,'VFA_Pet/anadirProd.html',contexto)

def Carrito(request):
    return render(request,'VFA_Pet/Carrito.html')

def Comprar(request):
    prod = Producto.objects.all()
    contexto ={
        "listaprodm": prod
    }
    return render(request,'VFA_Pet/Comprar.html',contexto)

def HistorialCompras(request):
    return render(request,'VFA_Pet/HistorialCompras.html')

def Inventario(request):
    invProd = Producto.objects.all()
    contexto ={
        "listaP": invProd
    }
    return render(request,'VFA_Pet/Inventario.html', contexto)

def ModificarProd(request, codProd):
    producto = Producto.objects.get(codProducto = codProd)
    catProd = Categoria.objects.all()
    contexto = {
        "datos": producto,
        "listacategorias": catProd
    }

    return render(request,'VFA_Pet/ModificarProd.html', contexto)


def MenuP(request):
    return render(request,'VFA_Pet/MenuP.html')

def ModificarContra(request):
    return render(request,'VFA_Pet/ModificarContra.html')

def Producto1(request,codigo):
    producto = Producto.objects.get(codProducto = codigo)
    contexto = {
        "prod": producto
    }
    return render(request,'VFA_Pet/Producto1.html',contexto)

def Producto2(request):
    return render(request,'VFA_Pet/Producto2.html')

def Producto3(request):
    return render(request,'VFA_Pet/Producto3.html')

def Producto4(request):
    return render(request,'VFA_Pet/Producto4.html')

def RecuperarContra(request):
    return render(request,'VFA_Pet/RecuperarContra.html')

def RegistroUsuario(request):
    arreglopreg = Pregunta.objects.all()
    contexto ={
        "pregunta": arreglopreg

    }
    return render(request,'VFA_Pet/RegistroUsuario.html',contexto)

def Ventas(request):
    Ventas = Venta.objects.all()
    contexto ={
        "listaVentas": Ventas
    }
    
    return render(request,'VFA_Pet/Ventas.html',contexto)

def ingresarProd(request):
    codprod = request.POST['cod_producto']
    nombrep = request.POST['Nombrep']
    stock = request.POST['Stock']
    descripcion = request.POST['Descripcion']
    foto = request.FILES['Foto']
    precio = request.POST['Precio']
    categoria = request.POST['ca_productos']

    catProd = Categoria.objects.get(idCategoria = categoria)

    Producto.objects.create(codProducto = codprod , nombreP = nombrep , stock = stock, descipcion = descripcion, foto = foto, precio = precio, categoria = catProd)
    return redirect('anadirProd')

def eliminarProd(request,codProd):
    producto = Producto.objects.get(codProducto = codProd)
    producto.delete()

    return redirect('Inventario')

def actualizarProducto(request):
    codprod = request.POST['cod_producto']
    nProd = request.POST['Nombrep']
    stockP = request.POST['Stock']
    descrP = request.POST['Descripcion']
    precioP = request.POST['Precio']
    catPro = request.POST['ca_productos']

    producto = Producto.objects.get(codProducto = codprod)
    producto.nombreP = nProd
    producto.stock = stockP
    producto.descipcion = descrP
    producto.precio = precioP
    registrocat = Categoria.objects.get(idCategoria = catPro)
    producto.categoria = registrocat

    producto.save()
    return redirect('Inventario')


def ingresarUser(request):
    rut = request.POST['rut']
    nombreu = request.POST['nameU']
    apellido = request.POST['Apellido']
    correo = request.POST['correo']
    fono = request.POST['fono']
    clave = request.POST['clave']
    idPregunta = request.POST['id_pregunta']
    respuesta = request.POST['respuesta']

    rolU = Rol.objects.get(idRol = 1)
    idpreg = Pregunta.objects.get(idPregunta = idPregunta)

    Usuario.objects.create(rut = rut , nombre = nombreu , apellido = apellido, correo = correo, fono = fono, clave = clave, rol = rolU, pregunta = idpreg, respuesta = respuesta)
    user = User.objects.create_user(correo, correo, clave)
    user.last_name = apellido
    user.save()
    return redirect('RegistroUsuario')

def iniciar_sesion(request):
    usuario1 = request.POST['correo']
    contra1 = request.POST['clave']
    try:
        user1 = User.objects.get(username = usuario1)
    except User.DoesNotExist:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect('MenuP')

    pass_valida = check_password(contra1, user1.password)
    if not pass_valida:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect('MenuP')
    usuario2 = Usuario.objects.get(correo = usuario1,clave = contra1)
    user = authenticate(username=usuario1, password=contra1)
    if user is not None:
        login(request, user)
        if(usuario2.rol.idRol == 2):
            return redirect('Inventario')
        else:
            contexto = {"usuario":usuario2 } 
            
            return render(request, 'VFA_Pet/Comprar.html', contexto)
            

