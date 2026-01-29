from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Etiqueta, Model3D


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'steam')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    list_filter = ('steam',)


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
        'preview_imagen',
        'image_url',   # ✅ así confirmas si el link está guardado
    )
    list_filter = (
        'categoria',
        'nivel',
        'etiquetas',   # ✅ útil cuando crezca tu catálogo
    )
    search_fields = (
        'nombre',
        'descripcion',
        'url_archivo',
        'image_url',   # ✅ encontrar por link
    )
    filter_horizontal = ('etiquetas',)
    ordering = ('nombre',)

    # ✅ Mostrar preview dentro del formulario
    readonly_fields = ('preview_imagen',)

    fields = (
        'nombre', 'descripcion',
        'image_url', 'imagen',
        'preview_imagen',   # ✅ lo ves antes de guardar
        'url_archivo',
        'categoria', 'etiquetas',
        'nivel',
    )

    def preview_imagen(self, obj):
        url = getattr(obj, "imagen_display", None)
        url = url() if callable(url) else url  # por si fuera método (seguro)
        if not url:
            return "—"
        return format_html(
            '<img src="{}" style="height:70px;border-radius:8px;object-fit:cover;" />',
            url
        )

    preview_imagen.short_description = "Imagen"
