# Generated by Django 3.2.4 on 2021-06-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0009_auto_20210619_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='ropa',
            name='inventario',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
