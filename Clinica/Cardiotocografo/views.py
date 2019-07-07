from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Persona
from .forms import PersonaForm


def registrada(request):
    return render(request, 'registrada.html',)

class PersonaCreate(CreateView):
    model = Persona
    fields = ('nombre', 'apellido', 'cedula', 'fecha_nac', 'sexo', 'telefono', 'direccion')
    template_name = 'persona_form.html'
    success_url = reverse_lazy('cardiotocografo')
