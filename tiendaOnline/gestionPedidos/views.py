from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import ropa






def inicio(request):
    return render(request, "inicio.html")
def servicios(request):
    return render(request, "servicios.html")
def contacto(request):
    return render(request, "contacto.html")
def dama(request):
    ropaDama=ropa.objects.filter(tipo='Falda en jean larga ¾.')
    return render(request, "dama.html",{"ropa":ropaDama})
def caballero(request):
    return render(request, "caballero.html")