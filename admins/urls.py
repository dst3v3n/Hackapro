from .views import Register_admin , Analisis
from django.urls import path

urlpatterns = [
    path('register/' , Register_admin.as_view() , name = 'register_admin'),
    path('analisis/' , Analisis.as_view() , name = 'analisis_power'),
]
