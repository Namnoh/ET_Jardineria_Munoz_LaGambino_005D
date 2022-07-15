from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Product, Miembro, Contacto, Customer, Boleta
from .forms import boletaForm, prodForm, miembroForm, contactoForm, formcrearCustomers
from  .Carrito import Carrito
from .context_processor import costo_envio, total_carrito
from datetime import date, timedelta
from django.contrib.auth.models import User
from .forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def galeria(request):
    productos = Product.objects.all()
    return render(request, 'galeria.html', {'productos':productos})

def somos(request):
    return render(request, 'somos.html')

def utilidades(request):
    return render(request, 'utilidades.html')

def contacto(request):
    if request.method=='POST':
        contacto = contactoForm(request.POST)
        if contacto.is_valid():
            contacto.save()
            return redirect('contacto')
    else:
            contacto = contactoForm()
    return render(request, 'contacto.html', {'contacto':contacto})

def miembros(request):
    if request.method=='POST':
        miembros = miembroForm(request.POST)
        if miembros.is_valid():
            miembros.save()
            return redirect('miembros')
    else:
        miembros = miembroForm()
    return render(request, 'miembros.html', {'miembros':miembros})

# EMPIEZA LO DE PRODUCTO
def showProd(request):
    products = Product.objects.all()

    datos = {
        'products' : products
    }
    return render(request, 'showProd.html', datos)

def formcrear_prod(request):
    if request.method=='POST':
        prod_form = prodForm(request.POST, files=request.FILES)
        if prod_form.is_valid():
            prod_form.save()
            return redirect('showProd')
    else:
        prod_form = prodForm()
    return render(request, 'formcrear_prod.html', {'prod_form': prod_form})

def formmod_prod(request, id):
    product = Product.objects.get(prodId=id)
    datos = {
        'form': prodForm(instance = product),
        'product': product,
    }
    if request.method == 'POST':
        if request.FILES != None:
            formulario = prodForm(data=request.POST, instance = product, files = request.FILES)
        else:
            formulario = prodForm(data=request.POST, instance = product)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('showProd')
    return render(request, 'formmod_prod.html', datos)

def del_prod(request, id):
    product = Product.objects.get(prodId=id)
    product.delete()
    return redirect('showProd')
# TERMINA LO DE PRODUCTO

# EMPIEZA LO DE CLIENTE
def formcrear_cust(request):
    if request.method=='POST':
        cliente = formcrearCustomers(request.POST)
        if cliente.is_valid():
            cliente.save()
            return redirect('showCustom')
    else:
        cliente = formcrearCustomers()
    return render (request, 'formcrear_cust.html', {'cliente':cliente})

def showCustom(request):
    clientes = Customer.objects.all()

    datos = {
        'clientes' : clientes
    }
    return render(request, 'showCustom.html', datos)

def formmod_cust(request, id):
    cliente = Customer.objects.get(custRut=id)
    datos = {
        'form2': formcrearCustomers(instance = cliente),
    }
    if request.method == 'POST':
        formulario = formcrearCustomers(data=request.POST, instance = cliente, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('showCustom')
    return render(request, 'formmod_cust.html', datos)

def del_cust(request, id):
    cliente = Customer.objects.get(custRut=id)
    cliente.delete()
    return redirect('showCustom')
# TERMINA LO DE CLIENTE

# EMPIEZO LO DEL CARRITO
def carrito (request):
    return render(request, "carrito.html")

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(prodId=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(prodId=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(prodId=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")
# TERMINA LO DEL CARRITO

# EMPIEZA LO DE BOLETA
def guardar_boleta(request, user_id):
    carrito = Carrito(request)
    productos = carrito.productos()
    cant = len(productos)
    if cant != 0:
        user = User.objects.get(id=user_id)
        cant=0
        for id in carrito.carrito.keys():
            if id in carrito.carrito.keys():
                stock = carrito.carrito[id]["cantidad"]
                cant+=stock
                producto = Product.objects.get(prodId=id)
                producto.prodStock = producto.prodStock - stock
                producto.save()
            elif id not in carrito.carrito.keys():
                while id not in carrito.carrito.keys():
                    id += 1
        total = sum(total_carrito(request).values())
        envio = sum(costo_envio(request).values())
        fechaC = date.today()
        fechaE = date.today() + timedelta(31)
        boleta = Boleta(bolProd=productos,bolCant=cant,bolEnvio=envio,bolTotal=total,bolDateC=fechaC,bolDateE=fechaE,bolCliId=user)
        boleta.save()
        carrito.limpiar()
        messages.success(request, "La compra ha sido exitosa.")
        return redirect("carrito")
    else:
        messages.error(request, 'El carrito está vacio')
        return redirect("carrito")
# TERMINA BOLETA

# EMPIEZA HISTORIAL DE COMPRA Y DETALLE.
def historial(request):
    context = {
        'boletas': Boleta.objects.all(),
    }
    return render(request, 'historial.html', context)

def detalle(request, bol_id):
    boleta = Boleta.objects.get(bolId=bol_id)
    fecha = request.POST.get('bolDateE')
    if request.method == 'POST':
        if fecha != None:
            boleta.bolDateE = fecha
            formulario = boletaForm(data=request.POST, instance = boleta)
            messages.success(request, "La fecha de entrega se ha cambiado exitosamente.")
            formulario.save()
        else:
            messages.error(request, 'Ha habido un error al intentar cambiar la fecha de entrega.')
            formulario = prodForm(data=request.POST, instance = boleta)
    boleta.refresh_from_db()
    context = {
        'boleta': boleta,
        'form': boletaForm(instance = boleta)
    }
    return render(request, 'detalle.html',context)

def historialCli(request,user_id):
    user = User.objects.get(id=user_id)
    
    try:
        boleta = Boleta.objects.filter(bolCliId=user)
    except Boleta.DoesNotExist:
        boleta = None
    context = {
        'boleta': boleta
    }
    return render(request, 'historialCli.html', context)

def detalleCli(request, bol_id):
    boleta = Boleta.objects.get(bolId=bol_id)
    context = {
        'boleta': boleta,
    }
    return render(request, 'detalleCli.html',context)

# TERMINA LO DE HISTORIAL Y DETALLE 

#COMIENZA LO DE REGISTRO 
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()

            # redirect user to home page
            messages.success(request, "Se ha registrado exitosamente.")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
# TERMINA LO DE REGISTRO