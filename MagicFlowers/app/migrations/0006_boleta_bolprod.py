# Generated by Django 4.0.4 on 2022-07-13 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_boleta_bolcustname_remove_boleta_bolcustrut_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='bolProd',
            field=models.CharField(default='----', max_length=1000, verbose_name='Productos'),
        ),
    ]
