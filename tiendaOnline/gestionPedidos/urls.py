from django.urls import path
from gestionPedidos import views

urlpatterns = [

    path('servicios/',views.servicios),
    path('tienda/dama/',views.dama),
    path('contacto/',views.contacto),
    path('inicio/',views.inicio),
    path('tienda/caballero/',views.caballero),
]
