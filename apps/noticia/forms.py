from dataclasses import field
from msilib.schema import Class
from django import forms
from .models import Noticia

class PostForm(forms.Form):

    class Meta:
        model = Noticia
        fields = ('título', 'texto',)
