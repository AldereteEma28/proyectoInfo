from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name="usuario"

urlpatterns = [
    path('register',views.register, name = 'register'),
    path('login/', LoginView.as_view(template_name='usuario/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'),name='logout'),
]