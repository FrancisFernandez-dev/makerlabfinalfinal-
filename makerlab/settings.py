import os
from pathlib import Path
import cloudinary
import cloudinary_storage

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# SEGURIDAD
# ==============================
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-dev-key")

# En Render, pon la variable de entorno DEBUG=True para ver errores detallados
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1,makerlabchile.onrender.com"
).split(",")

# Indispensable para que Render acepte subidas de formularios (POST)
CSRF_TRUSTED_ORIGINS = [
    "https://makerlabchile.onrender.com",
]

# Configuración de Cookies para HTTPS (Producción)
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

# ==============================
# APLICACIONES (El orden es vital)
# ==============================
INSTALLED_APPS = [
    'cloudinary_storage',  # DEBE IR ANTES DE STATICFILES
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'cloudinary',
    'biblioteca',
]

# ==============================
# MIDDLEWARE
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Para estáticos en Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'makerlab.urls'
WSGI_APPLICATION = 'makerlab.wsgi.application'

# ==============================
# TEMPLATES
# ==============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'biblioteca' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ==============================
# BASE DE DATOS
# ==============================
# Recuerda que en Render los datos de SQLite se borran al reiniciar/desplegar
# a menos que uses un disco persistente (Persistent Disk).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================
# CLOUDINARY & ALMACENAMIENTO
# ==============================
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.getenv("CLOUDINARY_API_KEY"),
    'API_SECRET': os.getenv("CLOUDINARY_API_SECRET"),
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ==============================
# ARCHIVOS ESTÁTICOS Y MEDIA
# ==============================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Obligatorio para construir las URLs de las fotos
MEDIA_URL = '/media/'

# ==============================
# AUTH & OTROS
# ==============================
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'inicio'
LOGOUT_REDIRECT_URL = 'inicio'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'