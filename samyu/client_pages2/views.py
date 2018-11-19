from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
from .f import detail_form
from .models import Amenities, Property_Upload, Hostel, Pricing_House
from client_pages2.models import detail
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import House

# disabling csrf (cross site request forgery)

def home(request):
    id=1
    list=[]
    addr=[]
    request.session['checkin'] = '24-12-18'

    hostdetails=[]
    area=[]
    if request.method == "POST":

        form = detail_form(request.POST)
        amenities = Property_Upload.objects.get(pr_id=id)
        pr_type = amenities.pr_type
        address=amenities.address

        host = amenities.user_id_id
        host = User.objects.get(id=host)
        hostdetails.append(host.first_name)
        hostdetails.append(host.email)
        if pr_type==0:

            hostel_id = Hostel.objects.get(pr_id_id=id)
            amenities = Amenities.objects.get(hostel_id=hostel_id)
            for am in amenities:
                list.append(am.amenities)

        if form.is_valid():
            detail_item = form.save(commit=False)
            detail_item.save()

            checkin = str(form.cleaned_data['checkin'])
            request.session['checkin'] = checkin

            checkout = str(form.cleaned_data['checkout'])
            request.session['checkout'] = checkout

            guests = form.cleaned_data['guests']
            request.session['guests'] = guests
            singlerooms = str(form.cleaned_data['rooms1'])
            request.session['rooms1'] = singlerooms
            singlerooms_attached = str(form.cleaned_data['rooms2'])
            request.session['rooms2'] = singlerooms_attached
            doublerooms = str(form.cleaned_data['rooms3'])
            request.session['rooms3'] = doublerooms
            doublerooms_attached = str(form.cleaned_data['rooms4'])
            request.session['rooms4'] = doublerooms_attached


            # print(request.session['guests'],request.session['checkin'])
    else:
        form = detail_form(initial={'checkin':request.session.get('checkin')})

    return render(request, 'client_pages2/html.html', {'form':form , 'list':list , 'hostdetails':hostdetails})





# Create your views here.
def default(request):
    initial_name = request.session['checkin']
    form = detail_form(initial={'checkout': initial_name})
    return render(request, 'client_pages2/html.html', {'form': form})