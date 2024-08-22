from django.shortcuts import render , redirect
from django.views.generic import View
from .forms import Form_actividad

# Create your views here.

class registro_actividad (View):
    template_name = 'from_registro_activity.html'

    def get (self, request):
        context = {
            'form_activity' : Form_actividad
        }
        return render(request , self.template_name, context)
    
    def post (self, request):
        form = Form_actividad(request.POST)
        if form.is_valid():
            info = form.save(commit = False)
            info.myuser_id = self.request.user.id
            info.save()
            return redirect ('registro_actividad')
