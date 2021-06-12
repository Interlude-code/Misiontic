from django.http import HttpResponse
import datetime
from django.template import Template,Context # añadir el import para usar Templat y Context

def saludo(request): #primera vista
    doc_open=open("C:/Users/Interlude/Desktop/Primer sitio web html/django\Misiontic/plantillas html/plantillaPagina.html")#abre el archivo donde esta el codigo html
    plt=Template(doc_open.read())##se lo lleva el objeto Templte el archivo se debe usar .red
    doc_open.close()#se cierra el archivo
    ctx= Context()#se crea el objeto Context si hay dinamicidad en la pagina en este caso sera vacio
    documento=plt.render(ctx)#se renderiza la pagina con .render la entrada de render sera el Context
    return HttpResponse(documento)
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
