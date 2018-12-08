from django.forms import ModelForm
from django import forms
from client_pages2.models import detail
from django import forms
import datetime



class detail_form(ModelForm):
    class Meta:
        model = detail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(detail_form, self).__init__(*args, **kwargs)
        d=2
        ch= [(X, X) for X in range(0,d)]
        self.fields['singlerooms'].choices = ch
        d2=4
        ch2 = [(X, X) for X in range(0, d2)]
        self.fields['singlerooms_attached'].choices = ch2
        d3=5
        ch3 = [(X, X) for X in range(0, d3)]
        self.fields['singlerooms_attached'].choices = ch3
        d4=6
        ch4 = [(X, X) for X in range(0, d4)]
        self.fields['doublerooms'].choices = ch4
        d5=4
        ch5 = [(X, X) for X in range(0, d5)]
        self.fields['doublerooms_attached'].choices = ch5





  #  def __init__(self, *args, request=None, **kwargs):
   #     super(detail_form, self).__init__(*args, **kwargs)
    #    self.request = request  # perhaps you want to set the request in the Form
     #   if request is not None:
      #      checkout = request.session['checkin']