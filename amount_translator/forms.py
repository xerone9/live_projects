from django import forms
from django.forms import ModelForm
from .models import UploadFile


class UploadFileForm(forms.Form):
    file = forms.FileField()
    # title = forms.CharField(max_length=50)
    # file = forms.FileField()
