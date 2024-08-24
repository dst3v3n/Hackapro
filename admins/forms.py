from django import forms
from .models import Myuser
from .admin import UserCreationForm

class Date (forms.DateInput):
    input_type = 'date'

class Form_myuser (UserCreationForm):
    check = forms.BooleanField(required = True , widget = forms.CheckboxInput(attrs={'class' : 'checkbox'}))
    class Meta:
        model = Myuser
        fields = ['name' , 'last_name' , 'gender' , 'birthdate' , 'email'] 

        widgets = {
            'name' : forms.TextInput(attrs = {
                'class' : 'controls',
                'placeholder' : 'Ingrese su Nombre' 
            }),

            'last_name' : forms.TextInput(attrs = {
                'class' : 'controls',
                'placeholder' : 'Ingrese su Apellido'
            }),

            'gender' : forms.Select(attrs = {'class' : 'controls'}),

            'birthdate' : Date(attrs = {'class' : 'controls'}),

            'email' : forms.EmailInput(attrs = {
                'class' : 'controls',
                'placeholder' : 'Ingrese su Correo'
            }),
        }

class Form_login (forms.ModelForm):
    password = forms.CharField (label = "password" , widget=forms.PasswordInput(attrs={
        'Placeholder' : 'Ingrese su contraseña',
        'id' : 'password',
        'class' : 'controls'
    }))

    class Meta:
        model = Myuser
        fields = ['email'] 

        widgets = {
            'email' : forms.TextInput(attrs = {'class' : 'controls', 'placeholder' : 'Ingrese su correo electronico'}),
        }

class Form_admin (UserCreationForm):
    check = forms.BooleanField(required = True , widget = forms.CheckboxInput(attrs={'class' : 'checkbox'}))
    class Meta:
        model = Myuser
        fields = ['name' , 'last_name' , 'gender' , 'birthdate', 'email'] 

        widgets = {
            'name' : forms.TextInput(attrs = {
                'class' : 'controls',
                'placeholder' : 'Ingrese su Nombre' 
            }),

            'last_name' : forms.TextInput(attrs = {
                'class' : 'controls',
                'placeholder' : 'Ingrese su Apellido'
            }),

            'gender' : forms.Select(attrs = {'class' : 'controls'}),

            'birthdate' : Date(attrs = {'class' : 'controls'}),

            'email' : forms.EmailInput(attrs = {
                'class' : 'controls',
                'placeholder' : 'Ingrese su Correo'
            }),
        }

