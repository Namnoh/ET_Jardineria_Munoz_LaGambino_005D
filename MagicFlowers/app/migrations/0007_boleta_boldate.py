# Generated by Django 4.0.4 on 2022-07-14 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_boleta_bolprod'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='bolDate',
            field=models.DateField(default=datetime.date(2022, 7, 13), verbose_name='Fecha'),
        ),
    ]