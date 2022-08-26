from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Categoria
from django.db.models import Q
from .forms import NoticiaForm,CategoriaForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import permission_required

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

@permission_required('is_staff')
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

@permission_required('is_staff')
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

@permission_required('is_staff')
def EliminarNoticia(request,noticia_id):
    try:
        noticia = Noticia.objects.get(pk = noticia_id)
        noticia.delete()
    except Noticia.DoesNotExist:
        raise Http404("Noticia no existe")
    return redirect('noticia:listarNoticia')

@permission_required('is_staff')
def crearCategoria(request):
    if request.method == "POST":
        addCategoria = CategoriaForm(request.POST)
        if addCategoria.is_valid():
            categoria = addCategoria.save(commit=False)
            categoria.save()
            return redirect('noticia:crearnoticia')
    else:
        addCategoria = CategoriaForm()
    return render(request, 'noticia/crearCategoria.html',{'addCategoria': addCategoria})