from django import forms
from .models import Model3D


class Model3DForm(forms.ModelForm):
    class Meta:
        model = Model3D
        fields = [
            'nombre',
            'descripcion',
            'image_url',     # ✅ AGREGAR
            'imagen',        # ✅ opcional
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
            'image_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://...jpg / png / webp'
            }),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'url_archivo': forms.URLInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'nivel': forms.Select(attrs={'class': 'form-select'}),
            'etiquetas': forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        image_url = cleaned_data.get("image_url")
        imagen = cleaned_data.get("imagen")

        # ✅ Evita que se guarde sin imagen
        if not image_url and not imagen:
            raise forms.ValidationError(
                "Debes agregar una imagen: pega un link (image_url) o sube un archivo (imagen)."
            )

        return cleaned_data
