from django.db import models

# Create your models here.

class categorias (models.Model):
    name = models.CharField(max_length = 35 , blank = False , null = False)

    class Meta:
       verbose_name = 'categorias'
       verbose_name_plural = 'categorias'
       db_table = 'categorias'
       ordering = ['name' , '-name']

class prediccion_power (models.Model):
    categoria = models.OneToOneField (
        categorias,
        models.CASCADE
    )
    valor = models.DecimalField(max_digits=10 , decimal_places=2)
