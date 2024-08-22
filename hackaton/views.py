from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import View

class index (View):
    template_name = 'index.html'

    def get (self, request: HttpRequest):
        
        return render(request, self.template_name)
