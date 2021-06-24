from django.contrib import admin
from gestionPedidos.models import ropa,clientes,categorias

'''# Register your models here.
class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre","documento")
    search_fields=('documento','email')'''
@admin.action(description='llenar mujeres')
def make_published(modeladmin, request, queryset):
    queryset.update(secciones='3')
class ropaAdmin(admin.ModelAdmin):
    list_display=('secciones','tallas','referencia','tipo')
    #search_fields=()
    list_filter=("precio",'tipo')
    actions = [make_published]
    

class cateroriasAdmin(admin.ModelAdmin):
    list_display=('categoria',)

    

admin.site.register(ropa,ropaAdmin,)
admin.site.register(clientes,)  
admin.site.register(categorias,cateroriasAdmin,)