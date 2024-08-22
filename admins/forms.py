from django import forms
from .models import Myuser
from .admin import UserCreationForm

class Date (forms.DateInput):
    input_type = 'date'

class Form_myuser (UserCreationForm):
    class Meta:
        model = Myuser
        fields = ['name' , 'last_name' , 'position' , 'gender' , 'birthdate', 'sector' , 'email'] 

        widgets = {
            'name' : forms.TextInput(attrs = {'class' : 'controls'}),
            'last_name' : forms.TextInput(attrs = {'class' : 'controls'}),
            'position' : forms.Select(attrs = {'class' : 'controls'}),
            'gender' : forms.Select(attrs = {'class' : 'controls'}),
            'sector' : forms.Select(attrs = {'class' : 'controls'}),
            'birthdate' : Date(attrs = {'class' : 'controls'}),
            'email' : forms.EmailInput(attrs = {'class' : 'controls'}),
        }

class Form_login (forms.ModelForm):
    password = forms.CharField (label = "password" , widget=forms.PasswordInput(attrs={
        'Placeholder' : 'Digite su contraseña',
        'id' : 'password',
        'class' : 'controls'
    }))

    class Meta:
        model = Myuser
        fields = ['email'] 

        widgets = {
            'email' : forms.TextInput(attrs = {'class' : 'controls'}),
        }
