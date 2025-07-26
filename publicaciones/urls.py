from django.urls import path
from . import views
from .views import CrearPublicacionView, MisPublicacionesView, ActualizarPublicacionView, EliminarPublicacionView

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_de_post'),
    path('publicacion-<int:pk>/', views.detalle_publicacion, name='detalle_post'),
    path('categoria-<int:pk>/', views.post_por_categoria, name='posts_por_categoria'),
    path('publicacion/crear/', CrearPublicacionView.as_view(), name='crear_publicacion'),
    path('mis-publicaciones/', MisPublicacionesView.as_view(), name='mis_publicaciones'),
    path('publicacion/<int:pk>/actualizar', ActualizarPublicacionView.as_view(), name='actualizar_publicacion'),
    path('publicacion/<int:pk>/eliminar', EliminarPublicacionView.as_view(), name='eliminar_publicacion'),
]