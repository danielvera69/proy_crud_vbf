from django.db import models

# Create your models here.
from django.db import models

class Doctor(models.Model):
    # Campo para el nombre del doctor (máximo 100 caracteres)
    first_name = models.CharField(max_length=100)
    
    # Campo para el apellido del doctor (máximo 100 caracteres)
    last_name = models.CharField(max_length=100)
    
    # Campo para la fecha de nacimiento del doctor
    birth_date = models.DateField()
    
    # Campo para la dirección del doctor (máximo 255 caracteres)
    address = models.CharField(max_length=255)
    
    # Campo booleano que indica si el doctor está activo o no (True por defecto)
    is_active = models.BooleanField(default=True)
    # La clase Meta es una forma de definir configuraciones adicionales que no pertenecen a los campos de datos directamente, sino a aspectos más globales del modelo
    class Meta:
        # Nombre singular del modelo en la administración
        verbose_name = "Doctor"
        
        # Nombre plural del modelo en la administración
        verbose_name_plural = "Doctores"
        
        # Ordenar por apellido y nombre
        ordering = ['last_name', 'first_name']
    
    # Método para devolver la representación del doctor como cadena de texto
    def __str__(self):
        # Devuelve el nombre y apellido del doctor
        return f"{self.first_name} {self.last_name}"
