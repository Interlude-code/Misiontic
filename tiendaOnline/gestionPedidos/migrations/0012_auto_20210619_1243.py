# Generated by Django 3.2.4 on 2021-06-19 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0011_auto_20210619_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ropa',
            old_name='fechaProduccion',
            new_name='fecha_Produccion',
        ),
        migrations.RenameField(
            model_name='ropa',
            old_name='resorteInterno',
            new_name='resorte_interno',
        ),
    ]
