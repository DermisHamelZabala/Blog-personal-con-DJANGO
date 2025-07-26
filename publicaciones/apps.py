from django.apps import AppConfig
# Importamos el módulo 'os' de Python, aunque en esta versión no lo usamos, 
# es útil para trabajar con el sistema operativo.

class PublicacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'publicaciones'
