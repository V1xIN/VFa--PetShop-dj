"""
URL configuration for VFA_PetShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from VFA_Pet.views import agregar_prod,eliminar_prod,restar_prod,limpiar_carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('VFA_Pet.urls')),
    path('rest/',include('rest_VfaPet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agregar_prod/<int:producto_id>/', agregar_prod,name="add"),
    path('eliminar/<int:producto_id>', eliminar_prod,name="Del"),
    path('restar/<int:producto_id>', restar_prod,name="Res"),
    path('limpiar', limpiar_carrito, name="limp"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
