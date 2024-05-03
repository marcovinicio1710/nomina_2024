# Generated by Django 5.0.1 on 2024-04-09 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOcs', '0009_remove_userprofile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contrasena_default',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Colaborador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='GOcs.colaboradores'),
        ),
    ]
