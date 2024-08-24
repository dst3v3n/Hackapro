from django.contrib import admin
from django.urls import path, include
from .views import registro_actividad , visualizar_actividad , Archivo

urlpatterns = [
    path('registro/', registro_actividad.as_view() , name='registro_actividad'),
    path("visualizar/" , visualizar_actividad.as_view(), name="visualizar_actividad"),
    path('archivo/', Archivo.as_view() , name = 'archivo')
]
