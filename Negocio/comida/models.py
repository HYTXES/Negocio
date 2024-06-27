from django.db import models

class Comida(models.Model):
 name = models.CharField(max_length=255)
 descripcion = models.TextField()
 precio = models.DecimalField(max_digits=10, decimal_places=2)
 stock = models.IntegerField()
 image = models.CharField(max_length=2083)
 

