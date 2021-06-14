from django.db import models

class clientes(models.Model):
        nombre=models.CharField(max_length=70)
        direccion=models.CharField(max_length=50)
        email=models.EmailField()
        telefono=models.CharField(max_length=10)
        documento=models.IntegerField()
class carros(models.Model):
    kilometraje=models.CharField(max_length=20)
    modelo=models.CharField(max_length=4)
    precio=models.IntegerField()
    inventario=models.IntegerField()
    siGas=models.BooleanField()
    siHybrido=models.BooleanField()
    marca=models.CharField(max_length=10)
