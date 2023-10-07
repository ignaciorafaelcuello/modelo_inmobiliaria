from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Inmueble(models.Model):
    direccion = models.CharField(max_length = 100)
    piso = models.IntegerField()
    depto = models.CharField(max_length = 3)
    precio = models.IntegerField()
    caracteristicas = models.CharField(max_length = 1000)
    fotos = models.ImageField(upload_to = 'inmuebles')

    def __str__(self):
        return f'{self.direccion}'
    
    class Meta:
        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'


class Avatar(models.Model):
    imagen = models.ImageField(upload_to = 'avatares')
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.imagen}'
    
class Presentacion(models.Model):
    pres = models.CharField(max_length = 100000000)


class Contacto(models.Model):
    nombre = models.CharField(max_length = 50, blank=False)
    apellido = models.CharField(max_length = 50, blank=False)
    correo = models.EmailField(blank = False)
    telefono = models.IntegerField(blank = False)
    
    def __str__(self):
        return f'{self.apellido, self.nombre}'
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

