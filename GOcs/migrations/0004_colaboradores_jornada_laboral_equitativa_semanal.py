# Generated by Django 5.0.1 on 2024-03-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOcs', '0003_planificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaboradores',
            name='Jornada_Laboral_Equitativa_Semanal',
            field=models.BooleanField(default=True, help_text='zipcode'),
        ),
    ]
