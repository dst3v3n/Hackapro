from django import forms
from .models import Actividades

class Form_actividad (forms.ModelForm):
    class Meta:
        model = Actividades
        fields = ['actividad' , 'descripcion']
        
        widgets = {
            'actividad' : forms.TextInput (attrs = {'class' : 'controls'}),
            'descripcion' : forms.Textarea (attrs = {
                'class' : 'controls',
                'cols': 10,
                'rows' : 2,
            })
        }
