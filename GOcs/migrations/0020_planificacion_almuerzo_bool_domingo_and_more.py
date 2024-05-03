# Generated by Django 5.0.1 on 2024-04-26 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOcs', '0019_archivos_colaboradores'),
    ]

    operations = [
        migrations.AddField(
            model_name='planificacion',
            name='Almuerzo_bool_Domingo',
            field=models.BooleanField(default=True, help_text='si debe tomar Hora Almuerzo'),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='Dia_Descanso_bool_Domingo',
            field=models.BooleanField(default=False, help_text='si toca descansar Domingo'),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='Entrada_Domingo',
            field=models.CharField(default='08:00', help_text='entrada de la jornada laboral', max_length=30),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='Hr_Laboradas_Domingo',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='Inicio_Hora_Almuerzo_Domingo',
            field=models.IntegerField(default=12, help_text='zipcode'),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='Jornada_Nocturna_bool_Domingo',
            field=models.BooleanField(default=False, help_text='si dpasar una noche al dia siguiente'),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='Salida_Domingo',
            field=models.CharField(default='08:00', help_text='entrada de la jornada laboral', max_length=30),
        ),
    ]
