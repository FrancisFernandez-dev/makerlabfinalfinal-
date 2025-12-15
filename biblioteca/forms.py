from django import forms
from .models import Model3D


class Model3DForm(forms.ModelForm):
    class Meta:
        model = Model3D
        fields = [
            'nombre',
            'descripcion',
            'imagen',        # 👈 CAMPO AGREGADO
            'url_archivo',
            'categoria',
            'etiquetas',
            'nivel'
        ]
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple()
        }
