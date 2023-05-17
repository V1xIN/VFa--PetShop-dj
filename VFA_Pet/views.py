from django.shortcuts import render

# Create your views here.

def anadirProd(request):
    return render(request,'VFA_Pet/anadirProd.html')

def Carrito(request):
    return render(request,'VFA_Pet/Carrito.html')

def Comprar(request):
    return render(request,'VFA_Pet/Comprar.html')

def HistorialCompras(request):
    return render(request,'VFA_Pet/HistorialCompras.html')

def Invetario(request):
    return render(request,'VFA_Pet/Invetario.html')

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