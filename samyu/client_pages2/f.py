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

       # ch = [(X, X) for X in range(0, d)]
        #self.fields['singlerooms_attached'].choices = ch
        #ch = [(X, X) for X in range(0, d)]
        #self.fields['doublerooms'].choices = ch
        #ch = [(X, X) for X in range(0, d)]
        #self.fields['doublerooms_attached'].choices = ch





  #  def __init__(self, *args, request=None, **kwargs):
   #     super(detail_form, self).__init__(*args, **kwargs)
    #    self.request = request  # perhaps you want to set the request in the Form
     #   if request is not None:
      #      checkout = request.session['checkin']