from django.http import HttpRequest
from django.shortcuts import render , redirect
from django.views.generic import View
from admins.forms import Form_myuser , Form_login
from django.core.exceptions import ValidationError
import sweetify
from django.contrib.auth import authenticate, logout , get_user_model
from django.contrib.auth import login as auth_login

class index (View):
    template_name = 'index.html'

    def get (self, request: HttpRequest):
        
        return render(request, self.template_name)

class registro (View):
    template_name = 'registro_us.html'
    
    def get (self, request: HttpRequest):
        context = {'form_register' : Form_myuser}
        return render(request, self.template_name, context)
    
    def post (self, request):
        email = request.POST ['email']
        password1 = request.POST ['password1']
        password2 = request.POST ['password2']
        form = Form_myuser(request.POST)
        if password1 and password2 and password1 == password2:
            if form.is_valid():
                form.save()
                sweetify.success (request, 'Cuenta creada', text='Tu cuenta ha sido creada', persistent='ok')
                return redirect ("registro")
        else:
            sweetify.error (request , "Las contraseñas no son iguales" ,  persistent='Ok')
            return redirect ("registro")

        sweetify.warning (request , "El correo ya existe" , persistent='Ok')
        return redirect ("registro")

class login (View):
    template_name = 'login_us.html'

    def get (self , request):
        context = {'form_login' : Form_login}        
        return render (request, self.template_name , context)

    def post (self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            response = redirect ('index')
            return response
        else:
            return redirect('login')

class logout_view (View):
    def get(self, request):
        logout(request)
        return redirect('index')
