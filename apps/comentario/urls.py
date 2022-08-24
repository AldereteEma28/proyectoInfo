from django.urls import path, re_path
from . import views

app_name="comentario"

urlpatterns = [
    path('<int:pk>/',views.add_comment_to_post, name = 'add_comment_to_post'),
]