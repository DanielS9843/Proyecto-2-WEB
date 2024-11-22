from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Importar Modelo
from.models import Campeon

# Create your views here.
def index(request):
    lista_campeones = Campeon.objects.all()
    template = loader.get_template("index.html")
    context = {"campeones":lista_campeones}
    return HttpResponse(template.render(context,request))


def vista_detalle(request, id_Campeon):
    # Consultar el registro en base de datos o devolver un 404 si no existe
    detalle_Campeon = Campeon.objects.get(id = id_Campeon)
    # Renderizar el template con el contexto
    template = loader.get_template("detail.html")

    context = {"Campeon":detalle_Campeon}
    return HttpResponse(template.render(context,request))
