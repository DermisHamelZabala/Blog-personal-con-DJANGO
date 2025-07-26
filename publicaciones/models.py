from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# se agrega encima de la clase Publicacion para poder pasar la clase Categoria como argumento
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class EstadoPublicacion(models.TextChoices):
    BORRADOR = 'BOR', 'Borrador'
    PENDIENTE = 'PEN', 'Pendiente'
    PUBLICADO = 'PUB', 'Publicado'

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='autor')

    # relacionando el modelo publicacion con categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='publicaciones')
    # primer argumento 'Categoria' indicar a que modelo se relaciona
    # segundo algumento 'on_delete=models.SET_NULL' para indicar que si se elimina una categoria las publicaciones no seran eliminadas
    # tercero y cuarto son necesarios para que funcione el segundo argumento
    # "related_name='publicaciones'" nos permite hacer consultas mas especificas usando el nombre publicaciones
    # ej: todas_publicaciones_categoria = categoria.publicaciones.all(), en vez de usar categoria.publicacion_set.all()

    estado = models.CharField(max_length=3, choices=EstadoPublicacion.choices, default=EstadoPublicacion.BORRADOR)

    # para ponerle el titulo a los registro en el admin de django
    def __str__(self):
        return self.titulo + " " + self.estado
    

