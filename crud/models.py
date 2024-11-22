from django.db import models

# Create your models here.
class Campeon(models.Model):
    nombre = models.CharField(max_length=200)
    rasgo_1 = models.CharField(max_length=200)
    rasgo_2 = models.CharField(max_length=200)
    coste = models.IntegerField(None)
    imagen = models.FileField(upload_to="campeones/")

    def __str__(self):
        return self.nombre