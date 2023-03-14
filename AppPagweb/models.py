from django.db import models

class Usuario(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField()
    Direccion = models.CharField(max_length=40)
     
    def __str__(self):
        return f"{self.id} - {self.Nombre}"
    
class Postear(models.Model):
    Animal = models.CharField(max_length=40)
    Edad = models.CharField(max_length=40)
    Caracteristicas = models.CharField(max_length=100)
    Mensaje = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.Animal}"

class Adoptame(models.Model):
    Animal = models.CharField(max_length=40)
    Caracteristicas = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.id} - {self.Animal}"