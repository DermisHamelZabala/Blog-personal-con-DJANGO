"""
en este archivo se crearan variables globales que se podran
usar en todos los templates(plantillas html).
"""
from .models import Categoria

def menu_categorias(request):
    # obteniendo todas las categorias
    categorias = Categoria.objects.all()

    return {'todas_las_categorias': categorias}