from django.db import models
from admins.models import Myuser
from .select import nucleo , respuesta , cargo , sector
from powerbi.models import categorias

# Create your models here.

class Perfil (models.Model):
    myuser = models.OneToOneField (
        Myuser,
        models.CASCADE
    )
    nucleo_familiar = models.CharField(max_length = 50, choices = nucleo() , default = '' , blank = False , null = False)
    cambios_trabajo = models.CharField(max_length = 40 , choices = respuesta() , default = 'Muy probable' , blank = False , null = False)
    tiempoDesplazamiento = models.DecimalField(max_digits=10, decimal_places=1)
    horasDomestica = models.DecimalField(max_digits=10, decimal_places=1)
    horasPersonal = models.DecimalField(max_digits=10, decimal_places=1)

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
    tiempoDedicado = models.DecimalField(max_digits=10, decimal_places=1)
    position = models.CharField (max_length = 105 , choices = cargo() , default = '' , null = True)
    sector = models.CharField (max_length = 105 , choices = sector() , default = '' , null = True)

    class Meta:
        verbose_name = 'trabajo'
        verbose_name_plural = 'trabajos'
        db_table = 'trabajos'
        ordering = ['myuser' , '-myuser']

class powerbi_user (models.Model):
    myuser = models.ForeignKey (
        Myuser,
        models.CASCADE
    )

    categoria = models.ForeignKey (
        categorias,
        models.CASCADE
    )

    valor = models.DecimalField(max_digits=10 , decimal_places=2)

    class Meta:
        verbose_name = 'powerbi_user'
        verbose_name_plural = 'powerbi_user'
        db_table = 'powerbi_user'
        ordering = ['myuser' , '-myuser']
