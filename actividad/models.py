from django.db import models
from admins.models import Myuser

# Create your models here.
class Actividades (models.Model):
    myuser = models.ForeignKey (
        Myuser,
        models.CASCADE
    )
    actividad = models.CharField (max_length = 30 , blank = False , null = False)
    descripcion = models.TextField ()
    
    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'
        db_table = 'actividades'
        ordering = ['actividad' , '-actividad']
