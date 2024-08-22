from django.contrib import admin
from django.urls import path, include
from .views import registro_actividad

urlpatterns = [
    path('registro/', registro_actividad.as_view() , name='registro_actividad'),
]
