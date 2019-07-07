from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Persona(models.Model):
  
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    cedula = models.CharField(max_length=11, primary_key=True,
    help_text="Ejemplo: V011223318",
    validators=[RegexValidator(regex="^[V|E]{1}[0]{1}[0-9]{7,9}$",
    message="Cedula ingresada incorrectamente, ingresarla nuevamente")])
    fecha_nac = models.DateField('Fecha de nacimiento', help_text="Año-Mes-Dia, Ej.: 2019-07-03")
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO)
    telefono = models.CharField(max_length=11, help_text="Ejemplo: 02742245565")
    direccion = models.CharField(max_length=150)

    class meta:
        ordering = ["nombre"] 

    def __str__(self):
        return self.cedula

    def get_absolute_url(self):
        return reverse('persona-detail', args=[str(self.cedula)])