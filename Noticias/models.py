from msilib.schema import Class
from django.db import models

# Create your models here.

class Noticia(models.Model):
   titulo = models.CharField(max_length=300, null=False)
   fecha = models.DateTimeField(auto_now_add=True)
   texto = models.TextField(null=True)
   activo = models.BooleanField(default=True)

  
