from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

def saludo(request):
    return HttpResponse("Hola Django-Coder")
def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto = f"Hoy es día: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    nombre = "Jimena"
    apellido = "Aznarez"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
    }

    #miHtml = open("/Users/jimenaaznarez/Desktop/Python/PythonProyecto1/Proyecto1/Proyecto1/plantilla")
    plantilla = loader.get_template("template1.html")
    #miHtml.close()
    #miContext = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)


