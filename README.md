# 🌐 Blog Personal con Django

Este repositorio contiene el resultado de un proyecto formativo completo en desarrollo web **full-stack**, combinando las mejores prácticas de **Django (backend)** con un **frontend moderno** y totalmente responsivo, desarrollado con **HTML5, CSS3 y JavaScript (Vanilla JS)**.

## 🔧 Tecnologías Utilizadas

- **Framework backend:** Django (Python)
- **Frontend:** HTML5, CSS3 (Flexbox, Grid, Variables), JavaScript puro
- **Base de datos:** POSTGRESQL
- **Autenticación:** Django Auth + vistas protegidas
- **Vistas:** Basadas en clases (CBV) y formularios personalizados

## ✨ Funcionalidades Clave

- Arquitectura MVT con separación clara de responsabilidades
- CRUD completo para publicaciones con relación a categorías y usuarios
- Panel de administración personalizado con filtros y visualización avanzada
- Sistema de autenticación completo (registro, login, logout)
- Búsqueda avanzada usando objetos `Q`
- Protección de vistas con `LoginRequiredMixin`
- Diseño totalmente responsivo usando Flexbox, CSS Grid y media queries
- Interactividad con JavaScript: menús desplegables, toggle de clases y manejo de eventos

## 🎯 Objetivo del Proyecto

Demostrar el desarrollo de una aplicación web funcional, robusta y bien estructurada utilizando herramientas modernas del ecosistema Python y tecnologías web. Este proyecto puede ser usado como base para blogs, portales informativos o plataformas de contenido.

## 📂 Estructura del Proyecto

- `publicaciones/`: Lógica principal de publicaciones, vistas y URLs
- `templates/`: Sistema de templates con `base.html` y herencia
- `static/`: Archivos de estilo y scripts JS personalizados
- `usuarios/`: Gestión de usuarios y autenticación
- `forms.py`: Formularios personalizados y validación
- `admin.py`: Panel de administración mejorado
