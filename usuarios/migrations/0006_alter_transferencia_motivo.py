# Generated by Django 5.1.3 on 2024-11-23 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_usuario_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferencia',
            name='motivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.motivotransferencia'),
        ),
    ]