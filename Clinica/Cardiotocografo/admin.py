from django.contrib import admin

# Register your models here.

from .models import Persona

#admin.site.register(Persona)
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'fecha_nac', 'sexo', 'telefono', 'direccion')