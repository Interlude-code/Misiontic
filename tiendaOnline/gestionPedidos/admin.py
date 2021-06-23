from django.contrib import admin
from gestionPedidos.models import ropa,clientes

'''# Register your models here.
class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre","documento")
    search_fields=('documento','email')'''
class ropaAdmin(admin.ModelAdmin):
    list_display=("tipo",'tallas','referencia')
    search_fields=('tipo',)
    list_filter=("precio",)

admin.site.register(ropa,ropaAdmin)
admin.site.register(clientes,)  