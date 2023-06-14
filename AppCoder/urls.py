from django.urls import path, include
from AppCoder.views import inicio, cursos, entregables, estudiante, profesores

urlpatterns = [ 
    path("inicio/", inicio),
    path("cursos/", cursos),
    path("entregables/", entregables),
    path("estudiante/", estudiante),
    path("profesores/", profesores),    
]
