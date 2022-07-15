from email.policy import default
import django
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class ProdCategory(models.Model):
    catId = models.BigAutoField(primary_key=True, verbose_name='Id de Categoría')
    catName =models.CharField(max_length=50, verbose_name='Nombre de la Categoría')

    def __str__(self):
        return self.catName

class Product (models.Model):
    prodId = models.BigAutoField(primary_key=True, verbose_name='Id del Producto')
    prodName = models.CharField(max_length=50, verbose_name='Nombre del Producto')
    prodPrice = models.IntegerField(verbose_name='Precio del Producto')
    prodBrand = models.CharField(max_length=50, default='' ,verbose_name='Marca del Producto')
    prodImage = models.ImageField(upload_to="products", verbose_name='Imagen del Producto', default=None)
    prodCat = models.ForeignKey(ProdCategory, on_delete=models.CASCADE, null=True)
    prodDesc = models.CharField(max_length=150, null=True,verbose_name='Descripción del Producto')
    prodStock = models.IntegerField(verbose_name='Stock del Producto', default=0)

    def __str__(self):
        return f'{self.prodId} - {self.prodName}'

class Customer (models.Model):
    custRut = models.CharField(primary_key=True,max_length=12,default=None, verbose_name='Rut')
    custName = models.CharField(max_length=25, verbose_name='Nombre del Cliente')
    custLastName = models.CharField(max_length=25, verbose_name='Apellido del Cliente')
    custEmail = models.CharField(max_length=25, verbose_name='Email del Cliente')
    custTel = models.IntegerField(verbose_name='Teléfono del Cliente')
    custComuna = models.CharField(max_length=15, verbose_name='Comuna del Cliente')
    custAddress = models.CharField(max_length=50, verbose_name='Direccion del Cliente',default='')
    custUser = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.custRut

class Boleta (models.Model):
    bolId = models.BigAutoField(primary_key=True, verbose_name='Id de Boleta')
    bolProd = models.CharField(max_length=1000, verbose_name='Productos', default="----")
    bolCant = models.IntegerField(verbose_name='Cantidad de los productos')
    bolEnvio = models.IntegerField(verbose_name='Valor Envio')
    bolTotal = models.IntegerField(verbose_name='Total')
    bolDateC = models.DateField(verbose_name='Fecha Compra', default=django.utils.timezone.now)
    bolDateE = models.DateField(verbose_name='Fecha Entrega', default=django.utils.timezone.now)
    bolCliId = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.bolId} - {self.bolDateC}'

class Miembro (models.Model):
    text1 = models.CharField(max_length=20, verbose_name='Nombre')
    text2 = models.CharField(max_length=20, verbose_name='Apellido')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    telefono = models.CharField(max_length=12, verbose_name='Teléfono')
    comunas = models.CharField(max_length=50, verbose_name='Comunas', default='')

    def __str__(self):
        return "Miembro"

class Contacto (models.Model):
    nombre1 = models.CharField(max_length=20, verbose_name='Nombre')
    nombre2 = models.CharField(max_length=20, verbose_name='Apellido')
    email = models.CharField(max_length=30, verbose_name='Correo')
    msg = models.CharField(max_length=600, verbose_name='Mensaje')

    def __str__(self):
        return "Contacto"
