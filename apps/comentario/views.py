from django.shortcuts import render, redirect, get_object_or_404
from apps.noticia.models import Noticia
from .forms import CommentForm
# Create your views here.
def add_comment_to_post(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.noticia = post
            comment.save()
            return redirect("noticia:detalleNoticia", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'noticia/add_comment_to_post.html', {'form': form})
