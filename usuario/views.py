from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente')
            return redirect('index')
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request, 'usuario/register.html',context)