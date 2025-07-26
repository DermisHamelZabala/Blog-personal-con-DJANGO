from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.vista_registro, name='registro')
]