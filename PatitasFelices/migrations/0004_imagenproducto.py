# Generated by Django 5.2.3 on 2025-05-21 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatitasFelices', '0003_turno_animal_turno_edad_mascota_turno_nombre_mascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='productos/imagenes_adicionales/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_adicionales', to='PatitasFelices.producto')),
            ],
        ),
    ]
