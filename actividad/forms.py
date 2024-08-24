from django import forms
from .models import Actividades

class Form_actividad (forms.ModelForm):
    class Meta:
        model = Actividades
        fields = ['actividad' , 'descripcion']
        
        widgets = {
            'actividad' : forms.TextInput (attrs = {'class' : 'controls',
                                                    'placeholder' : 'Ingrese la actividad'
                                                    }),
            'descripcion' : forms.Textarea (attrs = {
                'class' : 'controls',
                'cols': 10,
                'rows' : 2,
                'placeholder' : 'Ingrese la descripcion'
            })
        }
def validar_archivo_excel(file):
    if file.name.split('.')[-1].lower() not in ['xlsx', 'xls']:
        raise forms.ValidationError('Solo se aceptan archivos Excel (.xlsx, .xls)')
    return file

class Form_archivo (forms.Form):
    archivo = forms.FileField(
        label='Seleccione el archivo Excel',
        help_text='Solo se aceptan archivos Excel (.xlsx, .xls)',
        widget=forms.FileInput(attrs={
            'accept': '.xlsx, .xls',
            'class' : 'controls'
        }),
        validators=[validar_archivo_excel]
    )
