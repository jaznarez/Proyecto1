"""
URL configuration for Proyecto1 project.

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
from django.urls import path, include
from Proyecto1.view import probandoTemplate
from Proyecto1.view import saludo, segunda_vista, diaDeHoy, probandoTemplate


urlpatterns = [
    path(" ", saludo),
    path("admin/", admin.site.urls),
    path("saludo/", saludo), #http://127.0.0.1:8000/profesores/ esta es la ruta de acceso master al proyecto, para entrar al saludo de AppCoder sería:http://127.0.0.1:8000/AppCoder/profesores/ 
    path("segundavista/", segunda_vista),
    path("diadehoy/", diaDeHoy),
    path("probandotemplate/", probandoTemplate),
    path("AppCoder/", include("AppCoder.urls")), #esto es para relacionar las dos url, las de proyecto 1 directo, y las de AppCoder
]
