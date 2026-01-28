from django.contrib import admin
from django.utils.html import format_html
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
        'preview_imagen',
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

    # importante: incluir el campo en el formulario del admin
    fields = (
        'nombre', 'descripcion',
        'image_url', 'imagen',   # 👈 primero URL, luego subida
        'url_archivo',
        'categoria', 'etiquetas',
        'nivel',
    )

    def preview_imagen(self, obj):
        url = obj.imagen_display
        if not url:
            return "—"
        return format_html('<img src="{}" style="height:50px;border-radius:6px;" />', url)

    preview_imagen.short_description = "Imagen"
