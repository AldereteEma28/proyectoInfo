from django.shortcuts import render
from apps.noticia.models import Noticia

def Index(request):
    ultima_noticia = Noticia.objects.latest('fecha')
    context = {'ultima_noticia':ultima_noticia}
    return render(request, 'index.html',context)

