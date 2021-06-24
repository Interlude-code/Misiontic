from django.urls import path
from gestionPedidos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('servicios/',views.servicios),
    path('contacto/',views.contacto),
    path('inicio/',views.inicio),
    path('tienda/dama/',views.dama),
    path('tienda/caballero/',views.caballero),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)