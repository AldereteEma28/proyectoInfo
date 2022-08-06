from msilib.schema import Class
from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Noticia(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   titulo = models.CharField(max_length=300, null=False)
   fecha = models.DateTimeField(auto_now_add=True)
   texto = models.TextField(null=True)
   activo = models.BooleanField(default=True)
   imagen = models.ImageField(upload_to='noticia', default='Noticia/default.png')
   

  
