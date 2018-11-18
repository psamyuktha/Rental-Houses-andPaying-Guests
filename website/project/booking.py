from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking_House
from .models import Booking_Hostel

from django import forms



class booking_form(ModelForm):
    class Meta:
        model = Booking_House
        fields = '__all__'



class booking_form(ModelForm):
    class Meta:
        model = Booking_Hostel
        fields = '__all__'


