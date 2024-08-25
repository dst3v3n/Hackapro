from django.db import models
from admins.models import Myuser

# Create your models here.

class categorias (models.Model):
    name = models.CharField(max_length = 35 , blank = False , null = False)

    class Meta:
       verbose_name = 'categorias'
       verbose_name_plural = 'categorias'
       db_table = 'categorias'
       ordering = ['name' , '-name']

class prediccion_power (models.Model):
    categoria = models.ForeignKey (
        categorias,
        models.CASCADE
    )

    myuser = models.ForeignKey (
        Myuser,
        models.CASCADE,
        blank = True,
        null = True
    )

    valor = models.DecimalField(max_digits=10 , decimal_places=2)

    class Meta:
       verbose_name = 'prediccion_power'
       verbose_name_plural = 'prediccion_power'
       db_table = 'prediccion_power'
