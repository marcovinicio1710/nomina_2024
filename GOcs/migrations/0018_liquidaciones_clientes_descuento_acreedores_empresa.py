# Generated by Django 5.0.1 on 2024-04-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOcs', '0017_liquidaciones_descuento_acreedores_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquidaciones_clientes',
            name='Descuento_Acreedores_Empresa',
            field=models.FloatField(default=0),
        ),
    ]
