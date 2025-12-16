# 🧩 MakerLab Chile  
### Biblioteca Educativa de Modelos 3D

MakerLab Chile es una plataforma web orientada a la **educación STEAM**, que permite explorar, filtrar y acceder a **modelos 3D educativos** pensados para el aprendizaje activo en escuelas, hogares y espacios maker.

El proyecto combina desarrollo web con **Python y Django**, diseño UI moderno y una fuerte identidad **maker**, integrando tecnología, creatividad y educación.

---

## 🎯 Objetivo del proyecto

Desarrollar una biblioteca digital que facilite el acceso a modelos 3D educativos, fomentando:

- El aprendizaje práctico y experimental  
- El pensamiento crítico  
- La creatividad desde edades tempranas  
- La integración de la cultura maker en contextos educativos  

---

## 🛠️ Tecnologías utilizadas

- **Python 3.12**
- **Django 6**
- **HTML5**
- **CSS3 (estilos personalizados + Bootstrap 5)**
- **SQLite** (entorno de desarrollo)
- **Git & GitHub**

---

## ✨ Funcionalidades principales

- 📚 Biblioteca de modelos 3D educativos  
- 🔎 Búsqueda de modelos por nombre  
- 🧪 Filtrado por categorías **STEAM**:
  - Ciencia
  - Tecnología
  - Ingeniería
  - Artes
  - Matemáticas
- 🖼️ Visualización de imágenes de los modelos
- 🔗 Enlaces externos a repositorios (Cults, Thingiverse, Drive, etc.)
- 👤 Sistema de autenticación:
  - Registro de usuarios
  - Inicio y cierre de sesión
- ➕ Gestión de modelos (usuarios autenticados):
  - Agregar
  - Editar
  - Eliminar modelos

---

## 🧠 Enfoque educativo (STEAM)

MakerLab Chile está diseñado como un recurso pedagógico que apoya el enfoque **STEAM**, utilizando modelos 3D como herramientas didácticas para explicar conceptos complejos de forma visual y tangible.

---

## 🗂️ Estructura del proyecto

```text
makerlab/
│
├── biblioteca/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   └── img/
│   ├── templates/
│   │   ├── auth/
│   │   ├── biblioteca/
│   │   └── registration/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── makerlab/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── db.sqlite3
└── manage.py
