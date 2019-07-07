from django import forms
#from django.forms import ModelForm

from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'cedula',
            'fecha_nac',
            'sexo',
            'telefono',
            'direccion',
        ]
