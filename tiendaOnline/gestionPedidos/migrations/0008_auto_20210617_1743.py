# Generated by Django 3.2.4 on 2021-06-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0007_alter_carros_fechaingr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carros',
            name='fechaIngr',
        ),
        migrations.AddField(
            model_name='carros',
            name='fechaI',
            field=models.DateField(blank=True, null=True),
        ),
    ]
