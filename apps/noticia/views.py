from django.http import Http404
from django.shortcuts import render
from .models import Noticia

def detalleNoticia(request,noticia_id):
    try:
        noticia = Noticia.objects.get(pk = noticia_id)
    except Noticia.DoesNotExist:
        raise Http404("Pregunta no existe")
    return render(request,'noticia/detalleNoticia.html',{'noticia':noticia})

def listarNoticia(request):
    latest_noticie_list = Noticia.objects.order_by('-fecha')[:5]
    context = {'latest_noticie_list': latest_noticie_list}
    return render(request, 'noticia/listarNoticia.html',context)