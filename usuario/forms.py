from django import forms
from .models import Perfil , Trabajo

class Form_perfil (forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ['myuser']

        widgets = {
            'tiempoTrabajoRemota' : forms.NumberInput(attrs = {
                'max' : 24, 
                'min' : 0,
                'class' : 'controls',
                'placeholder' : 'Ingresa las horas que trabajas'
            }),
            'horasDomestica' : forms.NumberInput(attrs = {
                'max' : 24, 
                'min' : 0,
                'class' : 'controls',
                'placeholder' : 'Ingresa las horas haciendo labores domesticos'
            }),
            'horasPersonal' : forms.NumberInput(attrs = {
                'max' : 24, 
                'min' : 0,
                'class' : 'controls',
                'placeholder' : 'Ingresa las horas personales'
            }),
            'nucleo_familiar' : forms.Select(attrs = {'class' : 'controls'}),
            'ocupacion_actual' : forms.Select(attrs = {'class' : 'controls'}),
            'fomenta_trabajo' : forms.Select(attrs = {'class' : 'controls'}),
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
            'tiempoPreferido' : forms.NumberInput(attrs = {
                'max' : 100, 
                'min' : 0,
                'class' : 'controls',
                'placeholder' : 'Ingresa tu hora preferida para trabajar'
            }),
            'horasDedicada' : forms.NumberInput(attrs = {
                'max' : 100, 
                'min' : 0,
                'class' : 'controls',
                'placeholder' : 'Horas dedicadas al trabajo'
            }),
        }
