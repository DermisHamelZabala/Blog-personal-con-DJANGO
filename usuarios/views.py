from django.shortcuts import render, redirect
from .forms import FormularioRegistroUsuario
from django.contrib import messages # para mostrar mensajes
from django.contrib.auth import login


# Create your views here.

def vista_registro(request):
    # para detectar si un formulario ha sido enviado
    if request.method == 'POST':
        # pasando los datos de la peticion
        form = FormularioRegistroUsuario(request.POST)
        # comprobando si el formulario es valido
        if form.is_valid():
            # si es valido lo guardamos
            nuevo_usuario = form.save()
            # para mostrar un mensaje de exito
            messages.success(request, '¡Registro exitoso!')
            
            login(request, user=nuevo_usuario)
            
            # para redirigir al usuario a la pagina de inicio
            return redirect('lista_de_post')
    else:
        form = FormularioRegistroUsuario()
        

    
    context = {
        'form': form
    }

    return render(request, 'registration/registro.html', context)