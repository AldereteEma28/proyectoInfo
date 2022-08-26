from django.shortcuts import render,redirect, get_object_or_404
from .forms import CommentForm
from apps.noticia.models import Noticia
from django.contrib.auth.decorators import login_required

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.autor = request.user
            comment.noticia = post
            comment.save()
            return redirect('noticia:detalleNoticia', noticia_id=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comentario/crearComentario.html', {'form': form})