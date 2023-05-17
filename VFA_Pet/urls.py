from django.contrib import admin
from django.urls import path, include
from .views import home,index, contacto, borgona, borgona2

urlpatterns = [
    path('index',index,name="index"),
    path('',home,name="home"),
    path('contacto',contacto,name="contacto"),
    path('borgona',borgona,name="borgona"),
    path('borgona2',borgona2,name="borgona2"),
]