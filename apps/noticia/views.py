from django.http import Http404
from django.shortcuts import render
from .models import Noticia
from django.db.models import Q
from urllib.request import Request
from .forms import PostForm

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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
