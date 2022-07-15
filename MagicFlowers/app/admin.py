from django.contrib import admin
from .models import Product, Customer, ProdCategory, Miembro, Contacto, Boleta

# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ProdCategory)
admin.site.register(Miembro)
admin.site.register(Contacto)
admin.site.register(Boleta)