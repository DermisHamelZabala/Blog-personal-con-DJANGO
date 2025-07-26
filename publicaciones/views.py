from django.shortcuts import render
from .models import Publicacion, Categoria, EstadoPublicacion
from .forms import PublicacionForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

def lista_publicaciones(request):
    # obteniendo todas las publicaciones de la base de datos
    # Es la forma en Python de decir "SELECT * FROM publicaciones_publicacion;".
    busqueda = request.GET.get('buscar')
    lista_de_post = Publicacion.objects.filter(estado=EstadoPublicacion.PUBLICADO).order_by('-fecha_publicacion')

    if busqueda:
        lista_de_post = Publicacion.objects.filter(
            # usamos Q para buscar los registros de los campos incompletos, ignorando minusculas y mayusculas
            Q(titulo__icontains = busqueda) |
            Q(autor__username__icontains = busqueda)
        ).distinct().filter(estado=EstadoPublicacion.PUBLICADO)

    context = {
        'lista_de_post': lista_de_post
    }
    
    return render(request, 'publicaciones/lista_publicaciones.html', context)

def detalle_publicacion(request, pk):

    publicacion = Publicacion.objects.get(pk=pk)

    context = {
        'publicacion': publicacion
    }

    return render(request, 'publicaciones/detalle_post.html', context)


def post_por_categoria(request, pk):
    categoria_especifica = Categoria.objects.get(pk=pk)

    publicaciones_categoria = categoria_especifica.publicaciones.filter(estado=EstadoPublicacion.PUBLICADO).order_by('-fecha_publicacion')

    context = {
        'lista_de_post': publicaciones_categoria,
        'categoria_actual': categoria_especifica,
    }

    return render(request, 'publicaciones/lista_publicaciones.html', context)


class CrearPublicacionView(LoginRequiredMixin, CreateView):
    model=Publicacion
    form_class = PublicacionForm
    template_name='publicaciones/crear_publicacion.html'
    success_url=reverse_lazy('mis_publicaciones')

    def get_form_kwargs(self):
        # Tomamos los kwargs originales
        kwargs = super().get_form_kwargs()
        # Agregamos el usuario a los kwargs
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class MisPublicacionesView(LoginRequiredMixin, ListView):
    model = Publicacion
    template_name = 'publicaciones/mis_publicaciones.html'
    context_object_name = 'lista_de_estado_post'

    def get_queryset(self):        
        return Publicacion.objects.filter(autor=self.request.user).order_by('-fecha_publicacion')
    

class ActualizarPublicacionView(LoginRequiredMixin, UpdateView):
    model=Publicacion
    form_class = PublicacionForm
    template_name='publicaciones/crear_publicacion.html'
    success_url=reverse_lazy('mis_publicaciones')

    def get_form_kwargs(self):
        # Tomamos los kwargs originales
        kwargs = super().get_form_kwargs()
        # Agregamos el usuario a los kwargs
        kwargs['user'] = self.request.user
        return kwargs


class EliminarPublicacionView(LoginRequiredMixin, DeleteView):
    model=Publicacion
    success_url=reverse_lazy('mis_publicaciones')