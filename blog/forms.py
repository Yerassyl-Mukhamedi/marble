from django import forms

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Zapros
        fields = ('name', 'problem',)


class LaptopForm(forms.ModelForm):

    class Meta:
        model = Laptop
        fields = ('brand', 'name', 'family', 'company', 'inventNumber', 'serialNumber', 'owner')

class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ('name', 'surname', 'company', 'job')


class TonerForm(forms.ModelForm):

    class Meta:
        model = Toner
        fields = ('used_loads',)

class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ('name',)