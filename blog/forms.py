from django import forms

from .models import Zapros

class PostForm(forms.ModelForm):

    class Meta:
        model = Zapros
        fields = ('name', 'problem',)