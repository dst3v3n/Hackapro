from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class registro_actividad (View):
    template_name = 'from_registro_activity.html'

    def get (self, request):
        return render(request , self.template_name)
