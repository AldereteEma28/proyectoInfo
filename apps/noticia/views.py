from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia
from django.db.models import Q
from .forms import NoticiaForm
from django.utils import timezone

def detalleNoticia(request,noticia_id):
    try:
        noticia = Noticia.objects.get(pk = noticia_id)
    except Noticia.DoesNotExist:
        raise Http404("Noticia no existe")
    return render(request,'noticia/detalleNoticia.html',{'noticia':noticia})

def listarNoticia(request):
    busqueda = request.POST.get("buscar")
    latest_noticie_list = Noticia.objects.all().order_by('-fecha')
    if busqueda:
        latest_noticie_list = Noticia.objects.filter(
            Q(categoria__nombre__icontains = busqueda)|
            Q(titulo__icontains = busqueda)|
            Q(author__username__icontains = busqueda)
        ).distinct()
    context = {'latest_noticie_list': latest_noticie_list}
    return render(request, 'noticia/listarNoticia.html',context)

def crearNoticia(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.author = request.user
            noticia.save()
            return redirect('noticia:listarNoticia')
    else:
        form = NoticiaForm()
    return render(request, 'noticia/crearNoticia.html',{'form': form})

def editarNoticia(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.fecha = timezone.now()
            post.save()
            return redirect('noticia:listarNoticia')
    else:
        form = NoticiaForm(instance=post)
    return render(request, 'noticia/editarNoticia.html',{'form': form})