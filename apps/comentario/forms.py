from socket import fromshare
from django.forms import ModelForm
from django import forms 
from .models import comentario
#from principal.models import Comentario

# class ContactoForm(forms,Form):
#     correo = forms.EmailField(label="TU CORREO ELECTRONICO")
#     mensaje= forms.CharField(widget=forms.Textarea)

class CommentForm(ModelForm):

    class Meta:
        model = comentario
        fields = ('comentario',)