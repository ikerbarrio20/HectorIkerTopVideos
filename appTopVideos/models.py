from django.db import models
from datetime import datetime



class Categoria(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    videos = models.ManyToManyField('Video', blank=True, null=True)
    def __str__(self):
        return self.nombre


class Plataforma(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.  
    #logo = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image') #quizas tenemos que importar pillow
    videos = models.ManyToManyField('Video', blank=True, null=True)
    def __str__(self):
        return self.nombre

class Video(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    creador = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    categorias = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    #categorias = models.CharField(max_length=50)
    plataformas = models.ManyToManyField('Plataforma')
    #plataformas = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nombre
