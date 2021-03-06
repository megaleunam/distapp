# Generated by Django 2.0.3 on 2018-04-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=15, unique=True, verbose_name='Nombres del Estudiante')),
                ('nombres', models.CharField(default='', max_length=100, verbose_name='Nombres del Estudiante')),
                ('apellidos', models.CharField(default='', max_length=100, verbose_name='Nombres del Estudiante')),
                ('fecha_nac', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('celular', models.CharField(default='', max_length=20, verbose_name='Observaciones')),
                ('correo_electronico', models.EmailField(default='', max_length=250, verbose_name='correo electrónico')),
            ],
            options={
                'verbose_name_plural': 'estudiantes',
                'db_table': 'estudiantes',
                'verbose_name': 'estudiante',
            },
        ),
    ]
