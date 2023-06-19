from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    usuario1 = request.POST['correo']
    contra1 = request.POST['clave']
    try:
        user1 = User.objects.get(username=usuario1)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    
    pass_valida = check_password(contra1, user1.password)
    if not pass_valida:
        return Response("Password incorrecta")
    
    token, created = Token.objects.get_or_create(user=user1)
    
    return Response(token.key)
