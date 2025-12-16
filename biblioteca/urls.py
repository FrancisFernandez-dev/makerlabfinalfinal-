from django.urls import path
from . import views

urlpatterns = [
    # Inicio
    path('', views.inicio, name='inicio'),

    # Modelos
    path('modelos/', views.lista_modelos, name='lista_modelos'),
    path('agregar/', views.agregar_modelo, name='agregar_modelo'),
    path('editar/<int:pk>/', views.editar_modelo, name='editar_modelo'),
    path('eliminar/<int:pk>/', views.eliminar_modelo, name='eliminar_modelo'),

    # Páginas informativas
    path('contactanos/', views.contactanos, name='contactanos'),

    # Registro
    path('signup/', views.signup, name='signup'),
]

