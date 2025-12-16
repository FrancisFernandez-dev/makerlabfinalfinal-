from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Model3D, Category
from .forms import Model3DForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
def inicio(request):
    """
    Página principal con filtros STEAM
    """
    steam = request.GET.get('steam')

    modelos = Model3D.objects.all() \
        .select_related('categoria') \
        .prefetch_related('etiquetas')

    if steam:
        modelos = modelos.filter(categoria__steam=steam)

    categorias = Category.objects.all()

    return render(request, 'biblioteca/inicio.html', {
        'modelos': modelos,
        'categorias': categorias,
        'steam_activo': steam,
    })


def lista_modelos(request):
    """
    Lista avanzada con búsqueda + categoría + STEAM
    """
    categoria_id = request.GET.get('categoria')
    termino = request.GET.get('q')
    steam = request.GET.get('steam')

    modelos = Model3D.objects.all() \
        .select_related('categoria') \
        .prefetch_related('etiquetas')

    if categoria_id:
        modelos = modelos.filter(categoria_id=categoria_id)

    if termino:
        modelos = modelos.filter(nombre__icontains=termino)

    if steam:
        modelos = modelos.filter(categoria__steam=steam)

    categorias = Category.objects.all()

    return render(request, 'biblioteca/lista_modelos.html', {
        'modelos': modelos,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id,
        'termino_busqueda': termino,
        'steam_seleccionado': steam,
    })


@login_required
def agregar_modelo(request):
    if request.method == 'POST':
        form = Model3DForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = Model3DForm()

    return render(request, 'biblioteca/agregar_modelo.html', {'form': form})


@login_required
def editar_modelo(request, pk):
    modelo = get_object_or_404(Model3D, pk=pk)

    if request.method == 'POST':
        form = Model3DForm(request.POST, request.FILES, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = Model3DForm(instance=modelo)

    return render(request, 'biblioteca/editar_modelo.html', {
        'form': form,
        'modelo': modelo
    })


@login_required
def eliminar_modelo(request, pk):
    modelo = get_object_or_404(Model3D, pk=pk)

    if request.method == 'POST':
        modelo.delete()
        return redirect('lista_modelos')

    return render(request, 'biblioteca/confirmar_eliminar.html', {
        'modelo': modelo
    })


def contactanos(request):
    return render(request, 'biblioteca/contactanos.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login
            return redirect('inicio')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form
    })