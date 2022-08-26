from django import forms
from .models import Noticia, Categoria
class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'texto','imagen','categoria')

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nombre',)