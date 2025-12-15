from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Model3D, Category
from .forms import Model3DForm

def inicio(request):
    modelos = Model3D.objects.all().select_related('categoria').prefetch_related('etiquetas')
    categorias = Category.objects.all()

    return render(request, 'biblioteca/inicio.html', {
        'modelos': modelos,
        'categorias': categorias,
    })
    

def lista_modelos(request):
    """Vista para mostrar todos los modelos con la opción de filtrar por categoría y búsqueda"""
    categoria_id = request.GET.get('categoria')
    termino = request.GET.get('q')

    modelos = Model3D.objects.all().select_related('categoria').prefetch_related('etiquetas')

    if categoria_id:
        modelos = modelos.filter(categoria_id=categoria_id)

    if termino:
        modelos = modelos.filter(nombre__icontains=termino)

    categorias = Category.objects.all()

    context = {
        'modelos': modelos,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id,
        'termino_busqueda': termino,
    }
    return render(request, 'biblioteca/lista_modelos.html', context)

@login_required
def agregar_modelo(request):
    """Vista para agregar un nuevo modelo 3D"""
    if request.method == 'POST':
        form = Model3DForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = Model3DForm()
    return render(request, 'biblioteca/agregar_modelo.html', {'form': form})

@login_required
def editar_modelo(request, pk):
    """Vista para editar un modelo 3D existente"""
    modelo = get_object_or_404(Model3D, pk=pk)
    if request.method == 'POST':
        form = Model3DForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('lista_modelos')
    else:
        form = Model3DForm(instance=modelo)
    return render(request, 'biblioteca/editar_modelo.html', {'form': form, 'modelo': modelo})

@login_required
def eliminar_modelo(request, pk):
    """Vista para eliminar un modelo 3D"""
    modelo = get_object_or_404(Model3D, pk=pk)
    if request.method == 'POST':
        modelo.delete()
        return redirect('lista_modelos')
    return render(request, 'biblioteca/confirmar_eliminar.html', {'modelo': modelo})
