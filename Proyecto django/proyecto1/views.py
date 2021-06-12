from django.http import HttpResponse
import datetime
from django.template import Template,Context # añadir el import para usar Templat y Context
from django.template.loader import get_template
from django.shortcuts import render
def saludo(request): #primera vista
    nombre='caramela'
    ahora=datetime.datetime.now()
    lista1=['caramela','cururo','django','danco']
    #doc_open=open("C:/Users/Interlude/Desktop/Primer sitio web html/django\Misiontic/plantillas html/plantillaPagina.html")#abre el archivo donde esta el codigo html
    #plt=Template(doc_open.read())##se lo lle   va el objeto Templte el archivo se debe usar .red
    #doc_open.close()#se cierra el archivo
    #doc_open=get_template('plantillaPagina.html')
    #ctx= Context({'nombrePersona':nombre,'dia':ahora,'gatos':lista1})#se crea el objeto Context si hay dinamicidad en la pagina recibe diccionarios y objetos como entrada
    #documento=doc_open.render({'nombrePersona':nombre,'dia':ahora,'gatos':lista1})#se renderiza la pagina con .render la entrada de render sera el Context
    return render(request,'base.html',{'nombrePersona':nombre,'dia':ahora,'gatos':lista1}) #hace todo simplificado el request es obligatorio ,el siguiente es
                                                                                                        #la plantilla a renderizar ojo se debe tener en settings la carpeta y luego el diccionario del context y asi estaria todo 

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

def page2(request):
    lista1=[]
    ahora=datetime.datetime.now()
    return render(request,"plantillaPagina.html",{'dia':ahora,'gatos':lista1})