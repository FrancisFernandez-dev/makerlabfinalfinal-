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
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'url_archivo': forms.URLInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'nivel': forms.Select(attrs={'class': 'form-select'}),
            'etiquetas': forms.CheckboxSelectMultiple(),
        }