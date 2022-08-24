from django import forms
from .models import comentario
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):

    class Meta:
        model = comentario
        fields = ('comentario',)