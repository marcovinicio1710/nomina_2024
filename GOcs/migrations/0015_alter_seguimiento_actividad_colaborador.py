# Generated by Django 5.0.1 on 2024-04-10 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOcs', '0014_colaboradores_quien_agrego_jornada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento_actividad',
            name='Colaborador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='GOcs.colaboradores'),
        ),
    ]
