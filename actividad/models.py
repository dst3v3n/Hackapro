from django.db import models
from admins.models import Myuser
from .select import proceso

# Create your models here.
class Actividades (models.Model):
    myuser = models.ForeignKey (
        Myuser,
        models.CASCADE
    )
    actividad = models.CharField (max_length = 30 , blank = False , null = False)
    descripcion = models.TextField ()
    dateInicio = models.DateTimeField(null = True)
    dateFin = models.DateTimeField(null = True)
    proceso = models.CharField(max_length = 40 , choices = proceso() , default = 'Sin iniciar' , blank = False , null =False)
    tiempo = models.DurationField(null = True) 
    
    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'
        db_table = 'actividades'
        ordering = ['actividad' , '-actividad']

    @property
    def tiempo_formateado(self):
        diferencia = self.tiempo
        dias = diferencia.days
        horas = diferencia.seconds // 3600
        minutos = (diferencia.seconds // 60) % 60
        segundos = diferencia.seconds % 60

        if dias > 1:
            return f"{dias} días, {horas}:{minutos:02d}:{segundos:02d}"

        if dias == 1:
            return f"{dias} día, {horas}:{minutos:02d}:{segundos:02d}"

        if horas > 0:
            return f"{horas}:{minutos:02d}:{segundos:02d}"

        elif minutos > 0:
            return f"{minutos}:{segundos:02d}"
        
        else:
            return f"{segundos} segundos"
