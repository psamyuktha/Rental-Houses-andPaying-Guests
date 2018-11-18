import datetime
from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Booking_Hostel,Booking_House,Hostel,House,Property_Type,Pricing_House,Property_Upload,Pricing_Hostel
from .booking import booking_form
from .detail import detail_form
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
#
# def home(request):
#     hostel = Hostel.objects.get(avg_rating>=2)
#     list = []
#     for i in hostel:
#         id = i.pr_id
#         details = hostel_pricing.objects.get(i.pr_id)
#         dict = {gallery:i.gallery,  name:i.name, rating:i.avg_rating,description:i.description, price:details.price}
#         list.append(dict)
#
#     return render(request, 'project/nav.html' , list)


def home(request):
    if request.method == "POST":
        form = detail_form(request.POST)
        if form.is_valid():
            detail_item = form.save(commit=False)
            detail_item.save()
            place = form.cleaned_data['place']
            request.session['place'] = place
            checkin = str(form.cleaned_data['checkin'])
            request.session['checkin'] = checkin

            checkout = str(form.cleaned_data['checkout'])
            request.session['checkout'] = checkout

            guests = form.cleaned_data['guests']
            request.session['guests'] = guests
            form = detail_form()

            print(request.session['place'],request.session['guests'],request.session['checkin'])
    else:
        form = detail_form()
    return render(request, 'project/nav.html', {'form':form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('project:home')
    else:
        form = AuthenticationForm()
    return render(request, 'project/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'project/logout.html')
    else:
        logout(request)
        return render(request, 'project/logout.html')



@login_required(login_url='project:login')
def booking(request):
    if request.method == "POST":
        form = booking_form(request.POST)
        if form.is_valid():
            booking_item = form.save(commit=False)
            booking_item.save()
    else:
        form = booking_form()
    return render(request, 'project/booking_form.html', {'form':form})


@login_required(login_url='project:login')
def bookRoom(request):

    FirstDate = request.session['checkin']
    SecDate =  request.session['checkout']

    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin

    StayDuration = timedeltaSum.days

    request.session['single_a'] = 5
    request.session['single_wa'] = 5
    request.session['double_a'] = 5
    request.session['double_wa'] = 5
    request.session['triple_a'] = 5
    request.session['triple_wa'] = 5
    request.session['floorbed'] = 5

    property_id=1

    pricing = Pricing_House.objects.get(pr_id=property_id)

    cost_house = (request.session['single_a']) * (pricing.single_a) + (request.session['single_wa']) * (
        pricing.single_wa) + (request.session['double_a']) * (pricing.double_a) + (request.session['double_wa']) * (
                     pricing.double_wa) + (request.session['triple_a']) * (pricing.triple_a) + (
                 request.session['triple_wa']) * (pricing.triple_wa) + (request.session['floorbed']) * (
                     pricing.floorbed) + pricing.cleaning + pricing.security + pricing.extra

    total_cost = cost_house * StayDuration



    property = Property_Upload.objects.get(pr_id=property_id)
    street = property.address.street
    city = property.address.city
    state= property.address.state
    zipcode = property.address.zipcode

    images = House.objects.get(pr_id=property_id)
    image = images.gallery


    context = {'checkin': FirstDate, 'checkout':SecDate,'stayduration':StayDuration, 'image':image, 'totalcost':total_cost, 'street':street,'city':city,'state':state,'zipcode':zipcode}
    return render(request, 'project/booking_house.html', context)



def booking_house(request):
    FirstDate = request.session['checkin']
    SecDate = request.session['checkout']

    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin
    StayDuration = timedeltaSum.days

    request.session['single_a'] = 5
    request.session['single_wa'] = 5
    request.session['double_a'] = 5
    request.session['double_wa'] = 5
    request.session['triple_a'] = 5
    request.session['triple_wa'] = 5
    request.session['floorbed'] = 5

    property_id=1

    pricing = Pricing_House.objects.get(pr_id_id=property_id)

    user_id = request.user

    cost_house= (request.session['single_a'])*(pricing.single_a) + (request.session['single_wa'])*(pricing.single_wa) +(request.session['double_a'])*(pricing.double_a) +(request.session['double_wa'])*(pricing.double_wa)+ (request.session['triple_a'])*(pricing.triple_a) + (request.session['triple_wa'])*(pricing.triple_wa) + (request.session['floorbed'])*(pricing.floorbed)  + pricing.cleaning + pricing.security + pricing.extra

    total_cost = cost_house* StayDuration



    p=Booking_House.objects.create( check_in=FirstDate, check_out=SecDate, price_paid=total_cost,single_a = request.session['single_a'], single_wa= request.session['single_wa'], double_a=request.session['double_a'], double_wa=request.session['double_wa'], triple_a=request.session['triple_a'], triple_wa=request.session['triple_wa'],floorbed=request.session['floorbed'],Pr_id_id = property_id,user_id_id=1)
    p.save()

    return render(request, 'project/payment.html')



@login_required(login_url='project:login')
def bookHostel(request):
    FirstDate = request.session['checkin']
    SecDate = request.session['checkout']

    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin
    StayDuration = timedeltaSum.days

    request.session['single_a'] = 5
    request.session['single_wa'] = 5
    request.session['double_a'] = 5
    request.session['double_wa'] = 5
    request.session['triple_a'] = 5
    request.session['triple_wa'] = 5

    property_id = 1
    pricing = Pricing_Hostel.objects.get(pr_id_id=property_id)

    cost_hostel = (request.session['single_a'])*(pricing.single_a) + (request.session['single_wa'])*(pricing.single_wa) +(request.session['double_a'])*(pricing.double_a) +(request.session['double_wa'])*(pricing.double_wa)+ (request.session['triple_a'])*(pricing.triple_a) + (request.session['triple_wa'])*(pricing.triple_wa) + pricing.cleaning + pricing.security + pricing.extra + pricing.cab + pricing.food

    total_cost = cost_hostel * StayDuration


    property = Property_Upload.objects.get(pr_id=property_id)
    street = property.address.street
    city = property.address.city
    state= property.address.state
    zipcode = property.address.zipcode

    images = House.objects.get(pr_id=property_id)
    image = images.gallery


    context = {'checkin': FirstDate, 'checkout':SecDate,'stayduration':StayDuration, 'image':image, 'totalcost':total_cost, 'street':street,'city':city,'state':state,'zipcode':zipcode}
    return render(request, 'project/booking_hostel.html', context)





def booking_hostel(request):
    FirstDate = request.session['checkin']
    SecDate = request.session['checkout']

    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin
    StayDuration = timedeltaSum.days

    request.session['single_a'] = 5
    request.session['single_wa'] = 5
    request.session['double_a'] = 5
    request.session['double_wa'] = 5
    request.session['triple_a'] = 5
    request.session['triple_wa'] = 5

    user_id = request.user
    property_id = 1
    pricing = Pricing_Hostel.objects.get(pr_id_id=property_id)

    cost_hostel = (request.session['single_a'])*(pricing.single_a) + (request.session['single_wa'])*(pricing.single_wa) +(request.session['double_a'])*(pricing.double_a) +(request.session['double_wa'])*(pricing.double_wa)+ (request.session['triple_a'])*(pricing.triple_a) + (request.session['triple_wa'])*(pricing.triple_wa) + pricing.cleaning + pricing.security + pricing.extra + pricing.cab + pricing.food

    total_cost = cost_hostel * StayDuration

    p = Booking_Hostel.objects.create(check_in=FirstDate, check_out=SecDate, price_paid=total_cost, single_a = request.session['single_a'], single_wa=request.session['single_wa'], double_a=request.session['double_a'], double_wa=request.session['double_wa'], triple_a=request.session['triple_a'], triple_wa=request.session['triple_wa'],pr_id_id=property_id,user_id_id=1)
    p.save()

    return render(request, 'project/payment.html')


def cancelbooking(request):
    booking = Booking_House.objects.get(booking_id=11)
    booking.delete()
    currentuser = request.user
    link = reverse('project:viewbookings')
    return redirect(link)



def mybookings(request):
    bookings = Booking_House.objects.filter(user_id=1)
    context = {'bookings':bookings}
    return render(request, 'project/mybookings.html', context)


