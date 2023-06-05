from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from VFA_Pet.models import Usuario,Venta
from .serializers import Usuarioserializer,Ventaserializer
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])

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