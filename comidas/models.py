from django.db import models

class Lugar(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    def __unicode__(self):
        return self.nombre
class Restaurant(Lugar):
    sirve_hamburguesa = models.BooleanField()
    sirve_pizza = models.BooleanField()
    
    def __unicode__(self):
        return "Sirve Pizza %s" % self.sirve_pizza