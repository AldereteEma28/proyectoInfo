from django.urls import path, re_path
from . import views

app_name="noticia"

urlpatterns = [
    path('register',views.listarNoticia, name = 'listarNoticia'),
]