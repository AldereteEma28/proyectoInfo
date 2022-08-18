from django.db import models
from apps.noticia.models import Noticia

# Create your models here.
class comentario(models.Model):
   
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    comentario = models.TextField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comentario

"""class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, verbose_name= "Autor")
    text = models.TextField(verbose_name="Comentario")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text"""