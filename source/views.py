from django.shortcuts import render
from apps.noticia.models import Noticia
from django.contrib.auth.models import User

def Index(request):
    try:
        ultima_noticia = Noticia.objects.latest('fecha')
    except:
        autor = User.objects.get(username='admin')
        ultima_noticia = Noticia.objects.create(author=autor,titulo='simpletext')

    context = {'ultima_noticia':ultima_noticia}
    return render(request, 'index.html',context)

