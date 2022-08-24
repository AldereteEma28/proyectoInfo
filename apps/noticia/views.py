from django.http import Http404
from django.shortcuts import render, redirect 
from .models import Noticia
from django.db.models import Q

def EliminarNoticia(request,noticia_id):
    try:
        noticia = Noticia.objects.get(pk = noticia_id)
        noticia.delete()
    except Noticia.DoesNotExist:
        raise Http404("Pregunta no existe")
    return redirect('noticia:listarNoticia')

def detalleNoticia(request,noticia_id):
    try:
        noticia = Noticia.objects.get(pk = noticia_id)
    except Noticia.DoesNotExist:
        raise Http404("Pregunta no existe")
    return render(request,'noticia/detalleNoticia.html',{'noticia':noticia})

def listarNoticia(request):
    busqueda = request.POST.get("buscar")
    latest_noticie_list = Noticia.objects.all()
    if busqueda:
        latest_noticie_list = Noticia.objects.filter(
            Q(categoria__nombre__icontains = busqueda)
        ).distinct()
    context = {'latest_noticie_list': latest_noticie_list}
    return render(request, 'noticia/listarNoticia.html',context)
