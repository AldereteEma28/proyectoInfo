from django.shortcuts import render, redirect, get_object_or_404
from apps.noticia.models import Noticia
from .forms import CommentForm

# Create your views here.
def add_comment_to_post(Request):
    post = get_object_or_404(Noticia)
    if Request.method == "POST":
        form = CommentForm(Request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.noticia = post
            comment.save()
            return redirect("noticia:detalleNoticia")
    else:
        form = CommentForm()
    return render(Request, 'noticia/add_comment_to_post.html', {'form': form})
