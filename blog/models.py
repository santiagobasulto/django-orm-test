from django.db import models
import datetime

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def publicado_hoy(self):
        return self.pub_date.date() == datetime.date.today()
    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post)
    contenido = models.TextField()