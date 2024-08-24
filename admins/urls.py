from .views import Register_admin
from django.urls import path

urlpatterns = [
    path('register/' , Register_admin.as_view() , name = 'register_admin')

]
