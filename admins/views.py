from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from admins.forms import Form_admin
import sweetify

# Create your views here.

class Register_admin (LoginRequiredMixin , View):
    template_name = 'registro_us.html'

    def get(self, request):
        print(self.request.user.type_user)
        if self.request.user.type_user != 'User':
            context = {'form_register' : Form_admin}
            return render(request, self.template_name, context)
        
        else:
            return redirect ('index')

    
    def post(self , request):
        print('hola')
        email = request.POST ['email']
        password1 = request.POST ['password1']
        password2 = request.POST ['password2']
        form = Form_admin(request.POST)
        if password1 and password2 and password1 == password2:
            print(form)
            if form.is_valid():
                print(form)
                info = form.save(commit = False)
                info.type_user = 'Admin'
                info.save()
                sweetify.success (request, 'Cuenta creada', text='Tu cuenta ha sido creada', persistent='ok')
                return redirect ("register_admin")
        else:
            sweetify.error (request , "Las contraseñas no son iguales" ,  persistent='Ok')
            return redirect ("register_admin")

        sweetify.warning (request , "El correo ya existe" , persistent='Ok')
        return redirect ("register_admin")
