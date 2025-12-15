from django.contrib import admin
from .models import Category, Etiqueta, Model3D


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'categoria',
        'nivel',
    )
    list_filter = (
        'categoria',
        'nivel',
    )
    search_fields = (
        'nombre',
        'descripcion',
    )
    filter_horizontal = ('etiquetas',)
    ordering = ('nombre',)
