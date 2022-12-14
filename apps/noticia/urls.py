from django.urls import path, re_path
from . import views

app_name="noticia"

urlpatterns = [
    path('NoticiasMain',views.listarNoticia, name = 'listarNoticia'),
    path('<int:noticia_id>/', views.detalleNoticia, name = 'detalleNoticia'),
    path('post/<int:pk>/edit/', views.editarNoticia, name='editarNoticia'),
    path('noticia/new/', views.crearNoticia, name='crearnoticia'),
    path('<int:noticia_id>/eliminar',views.EliminarNoticia, name ='eliminarNoticia' ),
    path('crearCategoria/', views.crearCategoria, name = 'crearCategoria'),
]