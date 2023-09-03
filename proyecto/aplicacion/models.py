from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model): 
    nombre = models.CharField(max_length=50)
    DNI = models.IntegerField()
    email = models.EmailField() 

    def __str__(self):
        return f"{self.nombre}, {self.DNI}, {self.email}"

class Marca(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.marca}"

class Patente(models.Model):
    patente = models.CharField(max_length=8, blank=False)
    motor = models.IntegerField()

    def __str__(self):
        return f"{self.patente}"
    
class Problema(models.Model):
    reparar = models.CharField(max_length=50)  
    ingreso = models.DateField()
    entregado = models.BooleanField()   

    def __str__(self):
        return f"{self.reparar}"         
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"    