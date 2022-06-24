from random import choices
from xml.etree.ElementInclude import default_loader
from django.db import models

# Create your models here.

class  Parroquia(models.Model):
    opciones_tipo_parroquia =(
        ('urbana','Urbano'),
        ('rural','Rural')
    )

    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=opciones_tipo_parroquia)
    
    def __str__(self):
        return "%s %s" % (self.nombre, 
                self.tipo)

class  Barrio(models.Model):
    numero_parques =((1,'1'),(2,'2'),(3,'3'),(4,'4'),
    (5,'5'),(6,'6'))

    nombre = models.CharField(max_length=30)
    num_viviendas = models.IntegerField('numero de viviendas')
    num_parques = models.IntegerField(
    choices=numero_parques)
    num_edificios = models.IntegerField('numero de edificios')

    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE,
    related_name= "barrios")
    
    def __str__(self):
        return "%s %d %d %d" % (self.nombre, 
                self.num_viviendas,
                self.num_parques,
                self.num_edificios)

