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



class categorias(models.Model):
        categoria=models.CharField(max_length=50)
        class Meta:
                verbose_name="categorias"
                verbose_name_plural="categorias"
        def __str__(self):
                return self.categoria


class ropa(models.Model):
    tipo=models.CharField(max_length=40)
    precio=models.IntegerField()
    tallas=models.IntegerField()
    secciones=models.ForeignKey(categorias, on_delete=models.CASCADE, blank=True, null=True)
    material=models.CharField(max_length=70)
    resorte_interno=models.BooleanField()
    referencia=models.CharField(max_length=20)
    inventario=models.IntegerField()
    lote=models.CharField(max_length=50,blank=True, null=True)
    fecha_Produccion=models.DateField(blank=True, null=True)
    foto=models.ImageField(upload_to='ropa',blank=True, null=True)


        

    class Meta:
            verbose_name="prendas"
            verbose_name_plural="prendas"



