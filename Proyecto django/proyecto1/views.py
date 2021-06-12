from django.http import HttpResponse
import datetime

def saludo(request): #primera vista
    return HttpResponse("Esta es la primera pagina con django")
def despedida(request):
    return HttpResponse("adios django")
def fecha(request):
    fecha_actual=datetime.datetime.now()
    documento='''<html>
    <body>
    <h1>
    fecha y hora %s 
    </h1>
    <body/>
    <html/>''' % fecha_actual
    return HttpResponse(documento)
def calcularEdad(request,edad, anio):
    periodo= anio-2021
    edadFutra = edad + periodo
    documento='''<html>
    <body>
    <h1>
    en el año %s tendas %s 
    </h1>
    <body/>
    <html/>''' % (anio,edadFutra)
    return HttpResponse(documento)
