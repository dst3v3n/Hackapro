from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from admin.models import Myuser

# Register your models here.

class UserCreationForm (forms.ModelForm):
    password2 = forms.CharField (label = "password confirmation" , widget=forms.PasswordInput(attrs={
        'Placeholder' : 'Digite de nuevo la contraseña',
        'id' : 'passw',
        'class' : 'pass'
    }))
    password1 = forms.CharField (label = "password" , widget=forms.PasswordInput(attrs={
        'Placeholder' : 'Ingrese su contraseña, con un mínimo de 8 caracteres.',
        'id' : 'passw',
        'class' : 'pass'
    }))

    class Meta :
        model = Myuser
        fields = ['name' , 'email' ]

    def clean_password2 (self):
        password1 = self.cleaned_data.get ('password1')
        password2 = self.cleaned_data.get ('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError ("La contraseña no coincide")
        return password2

    def save (self, commit = True):
        user = super().save (commit=False)
        user.set_password (self.cleaned_data ["password1"])
        if commit:
            user.save ()
        return user

class UserChangeForm (forms.ModelForm):
    Password = ReadOnlyPasswordHashField()

    class Meta:
        model = Myuser
        fields = ['name' , 'password' ,'email' , 'type_user' , 'is_active' , 'is_admin']


class UserAdmin (BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email' , 'name' , 'type_user' , 'is_admin' , 'email_is_verified']
    list_filter = ['is_admin']
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ['name']}),
        ("Typer", {"fields": ['type_user']}),
        ("Permissions", {"fields": ["is_admin" , 'email_is_verified']}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", 'type_user' ,"password1", "password2"],
            },
        ),
    ]

    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(Myuser, UserAdmin)
admin.site.unregister(Group)
