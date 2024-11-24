# Generated by Django 5.1.3 on 2024-11-23 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0005_remove_cuenta_usuario'),
        ('usuarios', '0002_usuario_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cuenta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cuenta', to='transacciones.cuenta'),
        ),
    ]