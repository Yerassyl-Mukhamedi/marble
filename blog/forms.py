from django import forms

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Zapros
        fields = ('name', 'problem',)


class LaptopForm(forms.ModelForm):

    class Meta:
        model = Laptop
        fields = ('name', 'company', 'inventNumber', 'serialNumber', 'owner')

class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ('name', 'surname', 'company', 'job')
