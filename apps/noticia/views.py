from django.shortcuts import render

def listarNoticia(request):
    return render(request, 'noticia/listarNoticia.html')

