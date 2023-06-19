from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from VFA_Pet.models import Usuario,Venta
from .serializers import Usuarioserializer,Ventaserializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated))
def lista_Usuario(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = Usuarioserializer(usuario,many=True)
        return Response(serializer.data) 
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Usuarioserializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated))
def lista_Venta(request):
    if request.method == 'GET':
        ventas = Venta.objects.all()
        serializer = Ventaserializer(ventas,many=True)
        return Response(serializer.data) 
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Ventaserializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated))
def detalle_usuario(request,rut):

    try:
        usuario = Usuario.objects.get(rut=rut)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Usuarioserializer(usuario)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Usuarioserializer(usuario, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated))
def detalle_Venta(request, codVenta):

    try:
        venta = Venta.objects.get(codVenta = codVenta)
    except Venta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Ventaserializer(venta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Ventaserializer(venta, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.error,status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)