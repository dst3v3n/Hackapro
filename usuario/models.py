from django.db import models
from admins.models import Myuser
from .select import nucleo , ocupacion_actual , respuesta

# Create your models here.

class Perfil (models.Model):
    myuser = models.OneToOneField (
        Myuser,
        models.CASCADE
    )
    nucleo_familiar = models.CharField(max_length = 50, choices = nucleo() , default = '' , blank = False , null = False) 
    ocupacion_actual = models.CharField(max_length = 40 , choices = ocupacion_actual() , default = 'Trabajador' , blank = False , null = False)
    fomenta_trabajo = models.CharField(max_length = 40 , choices = respuesta() , default = 'Muy probable' , blank = False , null = False)
    cambios_trabajo = models.CharField(max_length = 40 , choices = respuesta() , default = 'Muy probable' , blank = False , null = False)
    tiempoTrabajoRemota = models.IntegerField()
    horasDomestica = models.IntegerField()
    horasPersonal = models.IntegerField()
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        db_table = 'perfiles'
        ordering = ['myuser' , '-myuser']

class Trabajo (models.Model):
    myuser = models.OneToOneField (
        Myuser,
        models.CASCADE
    )
    tiempoDedicado = models.IntegerField ()
    tiempoPreferido = models.IntegerField ()
    horasDedicada = models.IntegerField ()

    class Meta:
        verbose_name = 'trabajo'
        verbose_name_plural = 'trabajos'
        db_table = 'trabajos'
        ordering = ['myuser' , '-myuser']

