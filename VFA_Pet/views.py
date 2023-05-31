from django.shortcuts import render, redirect
from .models import Producto,Categoria

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
    return render(request,'VFA_Pet/Comprar.html')

def HistorialCompras(request):
    return render(request,'VFA_Pet/HistorialCompras.html')

def Invetario(request):
    invProd = Producto.objects.all()
    contexto ={
        "listaP": invProd
    }
    return render(request,'VFA_Pet/Invetario.html', contexto)

def MenuP(request):
    return render(request,'VFA_Pet/MenuP.html')

def ModificarContra(request):
    return render(request,'VFA_Pet/ModificarContra.html')

def Producto1(request):
    return render(request,'VFA_Pet/Producto1.html')

def Producto2(request):
    return render(request,'VFA_Pet/Producto2.html')

def Producto3(request):
    return render(request,'VFA_Pet/Producto3.html')

def Producto4(request):
    return render(request,'VFA_Pet/Producto4.html')

def RecuperarContra(request):
    return render(request,'VFA_Pet/RecuperarContra.html')

def RegistroUsuario(request):
    return render(request,'VFA_Pet/RegistroUsuario.html')

def Ventas(request):
    return render(request,'VFA_Pet/Ventas.html')

def ingresarProd(request):
    codprod = request.POST['cod_producto']
    nombrep = request.POST['Nombrep']
    stock = request.POST['Stock']
    descripcion = request.POST['Descripcion']
    foto = request.FILES['Foto']
    precio = request.POST['Precio']
    categoria = request.POST['productos']

    catProd = Categoria.objects.get(idCategoria = categoria)

    Producto.objects.create(codprod = codprod , nombreP = nombrep , stock = stock, descipcion = descripcion, foto = foto, precio = precio, categoria = catProd)
    return redirect('anadirProd')

def eliminarProd(request,codProd):
    producto = Producto.objects.get(codProducto = codProd)
    producto.delete()

    return redirect('Inventario')