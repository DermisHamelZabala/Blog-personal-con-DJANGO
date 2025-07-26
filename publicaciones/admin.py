from django.contrib import admin
from .models import Publicacion, Categoria

# 1. Importaciones iniciales
from django.apps import AppConfig
# Importamos el módulo 'os' de Python, aunque en esta versión no lo usamos, 
# es útil para trabajar con el sistema operativo.
import os 

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'
    
    # el metodo ready
    def ready(self):
        # 3. Importaciones diferidas
        from django.contrib.auth import get_user_model
        from decouple import config

        # 4. Condición de seguridad para ejecutar el código
        if config('CREATE_SUPERUSER', default=False, cast=bool):
            # 5. Obtención del modelo y las credenciales
            User = get_user_model()
            username = config('ADMIN_USERNAME', default='admin')
            email = config('ADMIN_EMAIL', default='admin@example.com')
            password = config('ADMIN_PASSWORD', default=None)

            # 6. Lógica de creación
            if password and not User.objects.filter(username=username).exists():
                print(f"Creando superusuario: {username}")
                User.objects.create_superuser(username=username, email=email, password=password)
            else:
                print("Superusuario ya existe o no se proporcionó contraseña de administrador.")


# Register your models here.


class PublicacionAdmin(admin.ModelAdmin):
    list_display=(
        'titulo',
        'autor',
        'categoria',
        'estado',
    )

    list_filter=(
        'estado',
        'autor',
    )

admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Categoria)