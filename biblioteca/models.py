from django.db import models

class Category(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.nombre


class Model3D(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    # 👇 CAMPO DE IMAGEN (NUEVO)
    imagen = models.ImageField(
        upload_to='modelos/',
        blank=True,
        null=True
    )

    url_archivo = models.URLField(
        help_text="Link a Thingiverse, Cults o Google Drive"
    )

    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name="modelos")

    nivel = models.CharField(
        max_length=20,
        choices=[
            ('Básico', 'Básico'),
            ('Intermedio', 'Intermedio'),
            ('Avanzado', 'Avanzado'),
        ]
    )

    def __str__(self):
        return self.nombre
