# Generated by Django 5.0.1 on 2024-03-29 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOcs', '0002_archivo_txt_dias_feriados_info_clientes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dia_Inicio_Planificacion', models.DateField(default='2024-01-02', help_text='dia entrada')),
                ('Dia_Salidad_Planificacion', models.DateField(default='2024-01-02', help_text='dia salida')),
                ('Hr_Laboradas_Lunes', models.FloatField()),
                ('Entrada_Lunes', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Salida_Lunes', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Almuerzo_bool_Lunes', models.BooleanField(default=True, help_text='si debe tomar Hora Almuerzo')),
                ('Inicio_Hora_Almuerzo_Lunes', models.IntegerField(default=12, help_text='zipcode')),
                ('Jornada_Nocturna_bool_Lunes', models.BooleanField(default=False, help_text='si dpasar una noche al dia siguiente')),
                ('Dia_Descanso_bool_Lunes', models.BooleanField(default=False, help_text='si toca descansar Lunes')),
                ('Hr_Laboradas_Martes', models.FloatField()),
                ('Entrada_Martes', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Salida_Martes', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Almuerzo_bool_Martes', models.BooleanField(default=True, help_text='si debe tomar Hora Almuerzo')),
                ('Inicio_Hora_Almuerzo_Martes', models.IntegerField(default=12, help_text='zipcode')),
                ('Jornada_Nocturna_bool_Martes', models.BooleanField(default=False, help_text='si dpasar una noche al dia siguiente')),
                ('Dia_Descanso_bool_Martes', models.BooleanField(default=False, help_text='si toca descansar Martes')),
                ('Hr_Laboradas_Miercoles', models.FloatField()),
                ('Entrada_Miercoles', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Salida_Miercoles', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Almuerzo_bool_Miercoles', models.BooleanField(default=True, help_text='si debe tomar Hora Almuerzo')),
                ('Inicio_Hora_Almuerzo_Miercoles', models.IntegerField(default=12, help_text='zipcode')),
                ('Jornada_Nocturna_bool_Miercoles', models.BooleanField(default=False, help_text='si dpasar una noche al dia siguiente')),
                ('Dia_Descanso_bool_Miercoles', models.BooleanField(default=False, help_text='si toca descansar Miercoles')),
                ('Hr_Laboradas_Jueves', models.FloatField()),
                ('Entrada_Jueves', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Salida_Jueves', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Almuerzo_bool_Jueves', models.BooleanField(default=True, help_text='si debe tomar Hora Almuerzo')),
                ('Inicio_Hora_Almuerzo_Jueves', models.IntegerField(default=12, help_text='zipcode')),
                ('Jornada_Nocturna_bool_Jueves', models.BooleanField(default=False, help_text='si dpasar una noche al dia siguiente')),
                ('Dia_Descanso_bool_Jueves', models.BooleanField(default=False, help_text='si toca descansar Jueves')),
                ('Hr_Laboradas_Viernes', models.FloatField()),
                ('Entrada_Viernes', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Salida_Viernes', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Almuerzo_bool_Viernes', models.BooleanField(default=True, help_text='si debe tomar Hora Almuerzo')),
                ('Inicio_Hora_Almuerzo_Viernes', models.IntegerField(default=12, help_text='zipcode')),
                ('Jornada_Nocturna_bool_Viernes', models.BooleanField(default=False, help_text='si dpasar una noche al dia siguiente')),
                ('Dia_Descanso_bool_Viernes', models.BooleanField(default=False, help_text='si toca descansar Viernes')),
                ('Hr_Laboradas_Sabado', models.FloatField()),
                ('Entrada_Sabado', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Salida_Sabado', models.CharField(help_text='entrada de la jornada laboral', max_length=30)),
                ('Almuerzo_bool_Sabado', models.BooleanField(default=True, help_text='si debe tomar Hora Almuerzo')),
                ('Inicio_Hora_Almuerzo_Sabado', models.IntegerField(default=12, help_text='zipcode')),
                ('Jornada_Nocturna_bool_Sabado', models.BooleanField(default=False, help_text='si dpasar una noche al dia siguiente')),
                ('Dia_Descanso_bool_Sabado', models.BooleanField(default=False, help_text='si toca descansar Sabado')),
                ('Cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='GOcs.info_clientes')),
                ('Colaborador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GOcs.colaboradores')),
            ],
        ),
    ]
