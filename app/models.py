from django.db import models

# Create your models here.

class Category(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class Book(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.name
