# Generated by Django 3.2.4 on 2021-06-23 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0018_rename_seccion_ropa_secciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ropa',
            name='secciones',
        ),
        migrations.AddField(
            model_name='ropa',
            name='seccion',
            field=models.ForeignKey(default='Dama', on_delete=django.db.models.deletion.CASCADE, to='gestionPedidos.categorias'),
            preserve_default=False,
        ),
    ]
