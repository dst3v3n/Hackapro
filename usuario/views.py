from django.shortcuts import render , redirect
from django.views.generic import View
from .forms import Form_perfil , Form_trabajo
from .models import Perfil , Trabajo
from admins.models import Myuser
from django.contrib.auth import logout
from marchine_learning.views import Modelo

# Create your views here.

class Perfil_view (View):
    template_name = 'perfil.html'

    def get (self, request):
        if Perfil.objects.filter(myuser_id = self.request.user.id).exists ():
            form_perfil = Form_perfil(instance = Perfil.objects.get(myuser_id = self.request.user.id))
            form_trabajo = Form_trabajo(instance = Trabajo.objects.get(myuser_id = self.request.user.id))

        else:
            form_perfil = Form_perfil
            form_trabajo = Form_trabajo

        context = {
            'form_perfil' : form_perfil,
            'form_trabajo' : form_trabajo
        }
        return render (request , self.template_name , context)

    def post (self, request):
        if request.POST.get('_method') == 'PUT':
            return self.put(request)

        elif request.POST.get('_method') == 'Eliminar':
            return self.delete(request)

        elif request.POST.get('_method') == 'CUENTA':
            return self.delete_cuenta(request)

        else:
            form_perfil = Form_perfil (request.POST)
            form_trabajo = Form_trabajo (request.POST)
            if form_perfil.is_valid ():
                print("hola")
                if form_trabajo.is_valid ():
                    print("hola")
                    info_perfil = form_perfil.save (commit = False)
                    info_perfil.myuser_id = self.request.user.id
                    info_perfil.save()

                    info_trabajo = form_trabajo.save(commit = False)
                    info_trabajo.myuser_id = self.request.user.id
                    info_trabajo.save ()
                    Modelo.conexion(self , self.request.user.id)

                    return redirect ('perfil_user')

            else:
                return redirect ('perfil_user')

    def put (self , request):
        perfil = Perfil.objects.get (myuser_id = self.request.user.id)
        form_perfil = Form_perfil (request.POST , instance = perfil)

        trabajo = Trabajo.objects.get (myuser_id = self.request.user.id)
        form_trabajo = Form_trabajo(request.POST , instance = trabajo)

        if form_perfil.is_valid():
            if form_trabajo.is_valid():
                form_perfil.save()
                form_trabajo.save()

                return redirect ('perfil_user')

        else:
            return redirect ('perfil_user')

    def delete (self, request):
        # Eliminar los datos en los modelos de prediccion
       perfil = Perfil.objects.get(myuser_id = self.request.user.id)
       perfil.delete()

       trabajo = Trabajo.objects.get(myuser_id = self.request.user.id)
       trabajo.delete()

       return redirect ('perfil_user')

    def delete_cuenta (self, request):
       usuario = Myuser.objects.filter(pk = self.request.user.id)
       usuario.delete()
       logout (request)

       return redirect('index')
