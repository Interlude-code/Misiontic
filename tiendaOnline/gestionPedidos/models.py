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
class carros(models.Model):
    kilometraje=models.CharField(max_length=20)
    modelo=models.CharField(max_length=4,verbose_name='Año de fabricacion')
    precio=models.IntegerField()
    inventario=models.IntegerField()
    marca=models.CharField(max_length=10)
    placa=models.CharField(max_length=10)
    fechaI=models.DateField(blank=True, null=True)
#carr1=carros(kilometraje='20000',modelo='corsa',precio=15000000,inventario=1,siGas=False,siHybrido=False,marca='renoult',placa='MIE88')       
    

    def __str__(self):
            return self.placa
