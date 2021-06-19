from django.contrib import admin
from gestionPedidos.models import carros,clientes

# Register your models here.
class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre","documento")
    search_fields=('documento','email')
class carrosAdmin(admin.ModelAdmin):
    list_display=("placa",)
    search_fields=('placa',)
    list_filter=("marca","fechaI")

admin.site.register(carros,carrosAdmin)
admin.site.register(clientes,clientesAdmin)