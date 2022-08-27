from django.db import models
from apps.noticia.models import Noticia
from django.contrib.auth.models import User

# Create your models here.
class comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE,related_name='comments')
    comentario = models.TextField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comentario
