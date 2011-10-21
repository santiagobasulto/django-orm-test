from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=False,auto_now_add=True)
    class Meta:
        abstract = True

class Nacional(Noticia):
    pueblo = models.CharField(max_length=200)
    
class Internacional(Noticia):
    pais = models.CharField(max_length=200)
    