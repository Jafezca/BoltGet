from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 256, blank = True, null = True)

    def __str__(self):
        return self.nombre


class Entrada(models.Model):
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=800)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)
    enlace = models.URLField()
    version = models.CharField(max_length=100, blank = True, null = True)
    nombre_archivo = models.CharField(max_length=256)
    fecha = models.DateField(auto_now_add=True)
    publicado = models.BooleanField()

    def __str__(self):
        return self.nombre

    def tipo(self):
        return 'entrada'
