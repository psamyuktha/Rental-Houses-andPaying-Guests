from django.contrib.auth.models import User
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
import client_pages2
from .f import detail_form
from .models import Amenities, Property_Upload, Hostel, Pricing_House
from client_pages2.models import detail
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import House,Gallery
from django.forms.models import modelformset_factory
pr_type=2
# disabling csrf (cross site request forgery)
def home(request):


    id=10
    house_id = House.objects.get(pr_id=id)

    addr=[]
    request.session['checkin'] = '20-8-2018'
    am = Property_Upload.objects.get(pr_id=id)
    #amenities = Amenities.objects.get(amenities)
    x= am.address.street+','+am.address.city

    #for am in amenities:
        #list.append(am.amenities)
    list=[]

    for y in Amenities.objects.filter():

         list.append(y)
    h=[]
    slide=Gallery.objects.filter()
    for i in slide:
        if i.pr.pr_id==10:

            h.append(i.img)



    #list = ["tv","hello"]
    hostdetails=[]
    area=[]

    image = house_id.gallery
    image2 = house_id.gallery1
    image3 = house_id.gallery2


    if request.method == "POST":

        form = detail_form(request.POST)

        pr_type = am.pr_type
       # address=amenities.address

        host = am.user_id_id
        host = User.objects.get(id=host)
        hostdetails.append(host.first_name)
        hostdetails.append(host.email)

        #if pr_type==1:


        #amenities = Amenities.objects.get(house_id=10)
        #for am in amenities:
               # list.append(am.amenities)
        checkin = request.session['checkin']
        checkout = request.session['checkout']

        guests = form.cleaned_data['guests']
        if form.is_valid():
            detail_item = form.save(commit=False)
            detail_item.save()



            #checkout = str(form.cleaned_data['checkout'])

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

    return render(request, 'client_pages2/html.html', {'h':h,'slide':slide,'form':form ,'image':image,'house_id':house_id,'image2':image2,'image3':image3, 'list':list , 'hostdetails':hostdetails,'address':x})
    #return HttpResponse(h)

def home2(request):
    id=10
    hostel_id = Hostel.objects.get(pr_id=id)

    addr=[]
    request.session['checkin'] = '20-8-2018'
    am = Property_Upload.objects.get(pr_id=id)
    #amenities = Amenities.objects.get(amenities)
    x= am.address.street+','+am.address.city

    #for am in amenities:
        #list.append(am.amenities)
    list=[]

    for y in Amenities.objects.filter():

         list.append(y)

    #list = ["tv","hello"]
    hostdetails=[]
    area=[]

    image = hostel_id.gallery
    image2 = hostel_id.gallery1
    image3 = hostel_id.gallery2

    if request.method == "POST":

        form = detail_form(request.POST)

        pr_type = am.pr_type
       # address=amenities.address

        host = am.user_id_id
        host = User.objects.get(id=host)
        hostdetails.append(host.first_name)
        hostdetails.append(host.email)

        #if pr_type==1:


        #amenities = Amenities.objects.get(house_id=10)
        #for am in amenities:
               # list.append(am.amenities)
        checkin = request.session['checkin']
        checkout = request.session['checkout']

        guests = form.cleaned_data['guests']
        if form.is_valid():
            detail_item = form.save(commit=False)
            detail_item.save()



            #checkout = str(form.cleaned_data['checkout'])

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

    return render(request, 'client_pages2/hostel.html', {'form':form ,'image':image,'house_id':hostel_id,'image2':image2,'image3':image3, 'list':list , 'hostdetails':hostdetails,'address':x})
    #return HttpResponse(image.url)


def type(request):
    if pr_type==2:
        return home(request)

    else:
       return home2(request)




# Create your views here.
