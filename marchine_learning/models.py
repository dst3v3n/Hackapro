from django.db import models
from admins.models import Myuser
from .categorizacion import cargo_catego , sector_catego , genero_catego , nucleo_catego , ocupacionActual_catego , respuesta_catego
from usuario.models import Trabajo , Perfil
from admins.models import Myuser

# Create your models here.

class Machine (models.Model):
    myuser = models.OneToOneField (
        Myuser,
        models.CASCADE
    )
    horasDomestica = models.IntegerField()
    tiempoDedicado = models.IntegerField()
    tiempoPreferido = models.IntegerField()
    horasDedicada = models.IntegerField()

    class Meta:
       verbose_name = 'Machine'
       verbose_name_plural = 'Machines'
       db_table = 'Machines'
       ordering = ['myuser' , '-myuser']

class Modelo:
    def categoria (self, id_user : int):
        data = Myuser.objects.filter(id_user).first()
        print(data)
        cargo = cargo_catego()[0]['']
