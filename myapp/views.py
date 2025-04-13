from django.shortcuts import render
from .forms import ProductoForm, CategoriaForm, ClienteForm, BuscarProductoForm
from .models import Producto

def index(request):
    return render(request, 'myapp/index.html')

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'myapp/formulario.html', {'form': form, 'titulo': 'Producto'})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'myapp/formulario.html', {'form': form, 'titulo': 'Categoría'})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'myapp/formulario.html', {'form': form, 'titulo': 'Cliente'})

def buscar_producto(request):
    resultado = []
    if request.method == 'GET':
        form = BuscarProductoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultado = Producto.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarProductoForm()
    return render(request, 'myapp/buscar.html', {'form': form, 'resultado': resultado})
