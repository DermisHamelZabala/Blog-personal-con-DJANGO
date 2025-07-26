from django.contrib import admin
from .models import Publicacion, Categoria

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