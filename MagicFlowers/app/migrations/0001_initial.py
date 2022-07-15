# Generated by Django 4.0.4 on 2022-06-27 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre1', models.CharField(max_length=20, verbose_name='Nombre')),
                ('nombre2', models.CharField(max_length=20, verbose_name='Apellido')),
                ('email', models.CharField(max_length=30, verbose_name='Correo')),
                ('msg', models.CharField(max_length=600, verbose_name='Mensaje')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('custRut', models.CharField(default=None, max_length=12, primary_key=True, serialize=False, verbose_name='Rut')),
                ('custName', models.CharField(max_length=25, verbose_name='Nombre del Cliente')),
                ('custLastName', models.CharField(max_length=25, verbose_name='Apellido del Cliente')),
                ('custEmail', models.CharField(max_length=25, verbose_name='Email del Cliente')),
                ('custTel', models.IntegerField(verbose_name='Teléfono del Cliente')),
                ('custComuna', models.CharField(max_length=15, verbose_name='Comuna del Cliente')),
                ('custAddress', models.CharField(max_length=50, null=True, verbose_name='Direccion del Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Miembros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(max_length=20, verbose_name='Nombre')),
                ('text2', models.CharField(max_length=20, verbose_name='Apellido')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=12, verbose_name='Teléfono')),
                ('comunas', models.CharField(default='', max_length=50, verbose_name='Comunas')),
            ],
        ),
        migrations.CreateModel(
            name='ProdCategory',
            fields=[
                ('catId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id de Categoría')),
                ('catName', models.CharField(max_length=50, verbose_name='Nombre de la Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prodId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id del Producto')),
                ('prodName', models.CharField(max_length=50, verbose_name='Nombre del Producto')),
                ('prodPrice', models.IntegerField(verbose_name='Precio del Producto')),
                ('prodBrand', models.CharField(default='', max_length=50, verbose_name='Marca del Producto')),
                ('prodImage', models.ImageField(default=None, upload_to='products', verbose_name='Imagen del Producto')),
                ('prodDesc', models.CharField(max_length=150, null=True, verbose_name='Descripción del Producto')),
                ('prodCat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.prodcategory')),
            ],
        ),
    ]
