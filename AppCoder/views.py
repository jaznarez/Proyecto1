from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request,"AppCoder/cursos.html") #tenemos que poner la ruta de donde estamos hasta llegar a cursos
                                                  #render como tal está hecho para buscar en la carpeta templates (si usamos render, hay que usar carpeta templates)
                                                  #render es la forma que se usa hoy en día para relacionar directamente un template con su método como tal (AppCoder en este caso) 
                                                  #En proyecto 1, la parte pricipal, usamos otra forma de relacionarlos que es la Dir url, en settings, pero se recomienda usar render.

def profesores(request):
    return render(request, "AppCoder/profesores.htm")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.htm")

