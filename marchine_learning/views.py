from django.shortcuts import render
from admins.models import Myuser
from usuario.models import Trabajo , Perfil
from .categorizacion import cargo_catego , sector_catego , genero_catego , nucleo_catego , ocupacionActual_catego , respuesta_catego

# Create your views here.

class Modelo:
    def categoria (self , id_user : int):
        data = Myuser.objects.get(pk = id_user)
        cargo = data.position
        id_catego = cargo_catego()[cargo]
