from django import forms
from .models import Publicacion, EstadoPublicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = (
            'titulo',
            'contenido',
            'estado',
            'categoria',
        ) 
    
    # para hacer obligatorio el campo categoria en el formulario
    def __init__(self, *args, **kwargs):
        # Tomamos el usuario del formulario si fue pasado como argumento
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Hacemos obligatorio el campo 'categoria'
        self.fields['categoria'].required = True
        self.fields['categoria'].error_messages = {'required': 'Por favor, introduce una categoria.'}

        # Filtrar opciones de estado para usuarios normales
        if user and not (user.is_staff or user.is_superuser):
            opciones_permitidas = [
                (EstadoPublicacion.BORRADOR, 'Borrador'),
                (EstadoPublicacion.PENDIENTE, 'Pendiente de Revisión'),
            ]
            self.fields['estado'].choices = opciones_permitidas