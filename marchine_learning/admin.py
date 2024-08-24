from django.contrib import admin
from .models import RegresionLogistica , RegresionLineal

# Register your models here.

admin.site.register(RegresionLineal)
admin.site.register(RegresionLogistica)
