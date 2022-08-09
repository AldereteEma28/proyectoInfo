from django.urls import path, re_path
from . import views

app_name="noticia"

urlpatterns = [
    path('NoticiasMain',views.listarNoticia, name = 'listarNoticia'),
    path('<int:noticia_id>/', views.detalleNoticia, name = 'detalleNoticia'),
]