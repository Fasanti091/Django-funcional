from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from datetime import datetime

def index(request, nombre):

    # Paso 0: Crear un contexto
    datos_contextos = {"fecha_actual": datetime.now(), "Username": nombre}

    # Paso 1: Cargar contenido HTML 
    archivo = open(r"D:\Estudios\CoderHouse - Python\Trabajos\Projects\MTV-Django\primer_mvt\primer_mvt\templates\index.html", "r")
    contenido_html = archivo.read()
    archivo.close()

    # Paso 2: Crear la plantilla
    plantilla = Template(contenido_html)

    # Paso 3: Crear contexto
    contexto = Context(datos_contextos)

    # Paso 4: Preparar documento para renderizar 
    documento_a_renderizar = plantilla.render(contexto)

    # Paso 5: Devolver la respuesta al usuaio
    return HttpResponse(documento_a_renderizar)

def notas(request):

    datos = {"notas":[9, 4, 3, 7, 10], "estudiante": "andres"}

    archivo = open(r"D:\Estudios\CoderHouse - Python\Trabajos\Projects\MTV-Django\primer_mvt\primer_mvt\templates\notas.html", "r")
    contenido = archivo.read()
    archivo.close()

    plantilla = Template(contenido)

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def alumnos(request):

    datos = {"curso": "Python", "alumnos": ["Santi","Aleja","Alejandro"]}

    plantilla = loader.get_template("alumnos.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)