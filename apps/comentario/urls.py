from django.urls import path
from . import views

app_name="comentario"

urlpatterns = [
        path('ComentariosMain',views.add_comment_to_post, name = 'add_comment_to_post'),
  ]