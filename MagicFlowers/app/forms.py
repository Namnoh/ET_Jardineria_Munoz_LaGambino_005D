from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Boleta, Product, Miembro, Contacto, Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class prodForm(forms.ModelForm):

    class Meta: 
        model= Product
        fields = '__all__'
        labels ={
            'prodId': 'Id',
            'prodName': 'Nombre',
            'prodPrice': 'Precio',
            'prodBrand': 'Marca',
            'prodImage': 'Imagen',
            'prodCat': 'Categoría',
            'prodDesc': 'Descripción',
            'prodStock': 'Stock'
        }
        widgets={
            'prodId': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Id', 
                    'id': 'prodId'
                }
            ), 
            'prodName': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Nombre', 
                    'id': 'prodName'
                }
            ), 
            'prodPrice': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Precio', 
                    'id': 'prodPrice'
                }
            ), 
            'prodBrand': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la Marca',
                    'id': 'prodBrand'
                }
            ),
            'prodImage': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'prodImage'
                }
            ),
            'prodCat': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'prodCat'
                }
            ),
            'prodDesc': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripción',
                    'id': 'prodDesc'
                }
            ),
            'prodStock': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Stock', 
                    'id': 'prodStock'
                }
            ), 
        }

comunas_choices= [
    ('Santiago', 'Santiago'),
    ('Maipu', 'Maipú'),
    ('Huechuraba','Huechuraba'),
    ('Las condes', 'Las Condes'),
    ('La reina','La Reina'),
    ('Independencia', 'Independencia')
]

class miembroForm(forms.ModelForm):

    class Meta: 
        model= Miembro
        fields = ['text1', 'text2', 'correo', 'telefono', 'comunas']

        labels ={
            'text1': 'Nombre',
            'text2': 'Apellido',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'comunas': 'Comunas',
        }
        widgets={
            'text1': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el nombre', 
                    'id': 'text1'
                }
            ), 
            'text2': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el apellido', 
                    'id': 'text2'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su correo', 
                    'id': 'correo'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su telefono',
                    'id': 'telefono'
                }
            ),
            'comunas': forms.Select(choices=comunas_choices
            ),
        }

class contactoForm(forms.ModelForm):

    class Meta:
        model= Contacto
        fields= ['nombre1','nombre2','email','msg']
        labels ={
            'nombre1': 'Nombre',
            'nombre2': 'Apellido',
            'email': 'Correo',
            'msg': 'Mensaje',
        }
        widgets={
            'nombre1': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el nombre', 
                    'id': 'nombre1'
                }
            ), 
            'nombre2': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el apellido', 
                    'id': 'nombre2'
                }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su correo', 
                    'id': 'email'
                }
            ), 
            'msg': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su mensaje',
                    'id': 'msg'
                }
            )
        }

class formcrearCustomers(forms.ModelForm):

    class Meta: 
        model= Customer
        fields = '__all__'
        labels ={
            'custRut': 'Rut',
            'custName': 'Nombre del cliente',
            'custLastName': 'Apellido del cliente',
            'custEmail': 'Correo',
            'custTel': 'Teléfono',
            'custComuna': 'Comuna',
            'custAddress': 'Dirección',
            'custUser': 'Usuario de Internet'
        }
        widgets={
            'custRut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su rut', 
                    'id': 'custRut'
                }
            ), 
            'custName': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Nombre', 
                    'id': 'custName'
                }
            ), 
            'custLastName': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el apellido', 
                    'id': 'custLastName'
                }
            ), 
            'custEmail': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo',
                    'id': 'custEmail'
                }
            ),
            'custTel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su telefono',
                    'id': 'custTel'
                }
            ),
            'custComuna': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'custComuna'
                },
                choices=comunas_choices
            ),
            'custAddress': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su dirección',
                    'id': 'custAddress'
                }
            ),
            'custUser': forms.Select(
                attrs={
                    'class': 'form-control',
                    'type': 'select',
                    'id': 'custUser'
                },
            ),
        }

class boletaForm(forms.ModelForm):

    class Meta:
        model = Boleta
        fields = ['bolDateE']
        labels = {
            'bolDateE': 'Fecha de Entrega'
        }
        widgets = {
            'bolDateE': forms.DateInput(
                attrs={
                    'type': 'date',
                    'id': 'bolDateE'
                }
            )
        }

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo'
        }