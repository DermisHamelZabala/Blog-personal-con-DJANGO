from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistroUsuario(UserCreationForm):
    # clase Meta para decir sobre que modelo trabajara el formulario y que campos mostrara
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )