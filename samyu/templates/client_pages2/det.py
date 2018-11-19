from django.forms import ModelForm
from django import forms
from samyuktha.models import detail
from django import forms



class detail_form(ModelForm):
    class Meta:
        model = detail
        fields = '__all__'

