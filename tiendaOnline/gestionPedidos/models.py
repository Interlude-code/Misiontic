from django.db import models

class clientes(models.Model):
        nombre=models.CharField(max_length=70)
        direccion=models.CharField(max_length=50)
        email=models.EmailField(blank=True, null=True)
        telefono=models.CharField(max_length=10)
        documento=models.IntegerField()
        #cliente1=clientes(nombre='',direccion='',email='',telefono='',documento='')
        def __str__(self):
                return self.nombre
class ropa(models.Model):
    tipo=models.CharField(max_length=40)
    precio=models.IntegerField()
    seccion=models.CharField(max_length=50)
    tallas=models.IntegerField()
    material=models.CharField(max_length=70)
    resorte_interno=models.BooleanField()
    referencia=models.CharField(max_length=20)
    inventario=models.IntegerField()
    lote=models.CharField(max_length=50,blank=True, null=True)
    fecha_Produccion=models.DateField(blank=True, null=True)



