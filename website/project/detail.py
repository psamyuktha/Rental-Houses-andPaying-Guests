from django.forms import ModelForm
from .models import detail

from django import forms



class detail_form(ModelForm):
    class Meta:
        model = detail
        fields = '__all__'
