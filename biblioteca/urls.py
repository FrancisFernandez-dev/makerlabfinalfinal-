from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Inicio
    path('', views.inicio, name='inicio'),

    # Modelos
    path('modelos/', views.lista_modelos, name='lista_modelos'),
    path('modelos/agregar/', views.agregar_modelo, name='agregar_modelo'),
    path('modelos/editar/<int:pk>/', views.editar_modelo, name='editar_modelo'),
    path('modelos/eliminar/<int:pk>/', views.eliminar_modelo, name='eliminar_modelo'),
     path('contactanos/', views.contactanos, name='contactanos'),

    # Autenticación
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='auth/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
