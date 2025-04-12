from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del trabajador o dispositivo
    latitud = models.FloatField()
    longitud = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.latitud}, {self.longitud}"
