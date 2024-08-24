from django.contrib import admin
from django.urls import path, include
from .views import Perfil_view

urlpatterns = [
    path ('crear/' , Perfil_view.as_view() , name = 'perfil_user')
]
