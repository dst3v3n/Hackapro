from django import forms
from .models import Perfil , Trabajo

class Form_perfil (forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ['myuser']

        widgets = {
            'horasDomestica' : forms.NumberInput(attrs = {
                'max' : 24, 
                'min' : 0,
                'class' : 'controls',
                'step': '0.1',
                'placeholder' : 'Ingresa las horas haciendo labores domesticos'
            }),
            'horasPersonal' : forms.NumberInput(attrs = {
                'max' : 24, 
                'min' : 0,
                'class' : 'controls',
                'step': '0.1',
                'placeholder' : 'Ingresa las horas personales'
            }),
            'tiempoDesplazamiento' : forms.NumberInput(attrs = {
                'max' : 24, 
                'min' : 0,
                'class' : 'controls',
                'step': '0.1',
                'placeholder' : 'Ingresa el tiempo de desplazamiento'
            }),
            'nucleo_familiar' : forms.Select(attrs = {'class' : 'controls'}),
            'cambios_trabajo' : forms.Select(attrs = {'class' : 'controls'}),
        }

class Form_trabajo (forms.ModelForm):
    class Meta:
        model = Trabajo
        exclude = ['myuser']

        widgets = {
            'tiempoDedicado' : forms.NumberInput(attrs = {
                'max' : 100, 
                'min' : 0,
                'class' : 'controls',
                'placeholder' : 'Ingresa el % de horas trabajadas en 3 meses'
            }),
            'position' : forms.Select(attrs = {'class' : 'controls'}),
            'sector' : forms.Select(attrs = {'class' : 'controls'}),
        }
