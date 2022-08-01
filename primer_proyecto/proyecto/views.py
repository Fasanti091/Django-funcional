from tkinter.font import families
from django.shortcuts import render
from django.http import HttpResponse
from proyecto.models import Curso
from django.template import Template, Context, loader

# Create your views here.

def lista_cursos(request):

    

    cursos = Curso.objects.all()

    familiares = {'curso':cursos}

    plantilla = loader.get_template("index.html")

    documento = plantilla.render(familiares)

    return HttpResponse(documento)