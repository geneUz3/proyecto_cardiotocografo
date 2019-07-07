from django.test import TestCase

# Create your tests here.

from .models import Persona


class PersonaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Persona.objects.create(
            nombre='Adrian',
            apellido='Uzcategui',
            cedula='V023777171',
            fecha_nac='2018-08-03',
            sexo = 'M',
            telefono= '02742666666',
            direccion= 'Av. Las Americas Sector Santo Domingo, Calle prinipal' )

    def test_fecha_nac_label(self):
        persona = Persona.objects.get(cedula='V023777171')
        field_label = persona._meta.get_field('fecha_nac').verbose_name
        self.assertEquals(field_label, 'Fecha de nacimiento')

    def test_nombre_max_length(self):
        persona = Persona.objects.get(cedula='V023777171')
        max_length = persona._meta.get_field('nombre').max_length
        self.assertEquals(max_length, 50)

    def test_apellido_max_length(self):
        persona = Persona.objects.get(cedula='V023777171')
        max_length = persona._meta.get_field('apellido').max_length
        self.assertEquals(max_length, 60)
    
    def test_cedula_max_length(self):
        persona = Persona.objects.get(cedula='V023777171')
        max_length = persona._meta.get_field('cedula').max_length
        self.assertEquals(max_length, 11)
    
    def test_sexo_max_length(self):
        persona = Persona.objects.get(cedula='V023777171')
        max_length = persona._meta.get_field('sexo').max_length
        self.assertEquals(max_length, 1)
    
    def test_telefono_max_length(self):
        persona = Persona.objects.get(cedula='V023777171')
        max_length = persona._meta.get_field('telefono').max_length
        self.assertEquals(max_length, 11)

    def test_direccion_max_length(self):
        persona = Persona.objects.get(cedula='V023777171')
        max_length = persona._meta.get_field('direccion').max_length
        self.assertEquals(max_length, 150)
        