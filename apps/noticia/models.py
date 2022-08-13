import datetime
from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
   nombre = models.CharField(max_length=300, null=False)

   def __str__(self):
      return self.nombre

class Noticia(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   titulo = models.CharField(max_length=300, null=False)
   fecha = models.DateTimeField(auto_now_add=True)
   texto = models.TextField(null=True)
   activo = models.BooleanField(default=True)
   categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
   imagen = models.ImageField(upload_to='noticia', default='noticia/default.png')
   
   def __str__(self):
      return self.titulo
   
   def publicacion_reciente(self):
      return self.fecha >=timezone.now() - datetime.timedelta(days=1)