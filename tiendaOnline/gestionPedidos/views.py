from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import ropa






def inicio(request):
    return render(request, "inicio.html")
def servicios(request):
    return render(request, "servicios.html")
def dama(request):
    return render(request, "dama.html")
def caballero(request):
    return render(request, "caballero.html")
def contacto(request):
    return render(request, "contacto.html")