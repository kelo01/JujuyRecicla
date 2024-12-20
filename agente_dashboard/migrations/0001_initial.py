# Generated by Django 5.1.3 on 2024-12-03 10:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('mantenimiento', 'Mantenimiento'), ('lleno', 'Módulo Lleno'), ('danio', 'Daño Reportado')], max_length=20)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('activa', 'Activa'), ('en_proceso', 'En Proceso'), ('resuelta', 'Resuelta')], default='activa', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('puntos_requeridos', models.IntegerField()),
                ('puntos_otorgados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('ubicacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('puntos_por_kg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=200)),
                ('direccion_detallada', models.TextField(blank=True)),
                ('capacidad_total', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('capacidad_actual', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='modulos/')),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('mantenimiento', 'En Mantenimiento'), ('lleno', 'Lleno')], default='disponible', max_length=20)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('horario', models.CharField(default='24/7', max_length=200)),
            ],
            options={
                'verbose_name': 'Módulo',
                'verbose_name_plural': 'Módulos',
            },
        ),
    ]
