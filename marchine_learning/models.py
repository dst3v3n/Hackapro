from django.db import models
from admins.models import Myuser

# Create your models here.

class RegresionLogistica (models.Model):
    myuser = models.OneToOneField (
        Myuser,
        models.CASCADE
    )
    trabajoRemoto = models.CharField(max_length = 35 , blank = False , null = False)

    class Meta:
       verbose_name = 'RegresionLogistica'
       verbose_name_plural = 'RegresionesLogisticas'
       db_table = 'RegresionLogistica'
       ordering = ['myuser' , '-myuser']

class RegresionLineal (models.Model):
    myuser = models.OneToOneField (
        Myuser,
        models.CASCADE
    )
    trabajoRemoto = models.IntegerField

    class Meta:
       verbose_name = 'RegresionLineal'
       verbose_name_plural = 'RegresionesLineales'
       db_table = 'RegresionLineal'
       ordering = ['myuser' , '-myuser']
