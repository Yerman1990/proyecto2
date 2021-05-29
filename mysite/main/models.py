from django.db import models
class Curso(models.Model):
    curso_titulo = models.CharField(max_length=200)
    curso_contenido = models.TextField()
    curso_publicado = models.DateField("fecha de publicación")
    def _str_(self):
        return self.curso_titulo


