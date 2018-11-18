from django.shortcuts import render,redirect
from hostupload.forms import AddressForm,Pricing_HostelForm,Pricing_HouseForm,UploadForm,HostelForm,HouseForm
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from hostupload.models import Property_Upload,Hostel,Amenities
from django.contrib.auth.models import User


def UploadHostelview(request):

    if request.method=='POST':
        hostel = HostelForm(data=request.POST)
        price = Pricing_HostelForm(data=request.POST)
        pid = request.session.get('property')
        Property_Uplo = Property_Upload.objects.get(id=pid)

        if hostel.is_valid() and price.is_valid():
            hostelinstance = hostel.save(commit=False)
            hostelinstance.pr = Property_Uplo
            priceinstance = price.save(commit=False)
            priceinstance.pr = Property_Uplo
            priceinstance.save()
            price.save()
            hostelinstance.price = priceinstance
            hostel_instance=hostel.save()
            for amenity in hostel_instance.amenities.all():
                hostel_instance.amenities.add(amenity)
                hostel_instance.save()

            return render(request,'hostupload/done.html')

    else:
        hostel = HostelForm()
        price = Pricing_HostelForm()
        return render(request,'hostupload/hostel.html',{'hostel':hostel,'price':price})

def UploadHouseview(request):

    if request.method=='POST':
        house = HouseForm(data=request.POST)
        price = Pricing_HouseForm(data=request.POST)
        pid =  request.session.get('property')
        Property_Uplo = Property_Upload.objects.get(id=pid)

        if house.is_valid() and price.is_valid():
            houseinstance = house.save(commit=False)
            houseinstance.pr = Property_Uplo
            priceinstance = price.save(commit=False)
            priceinstance.pr = Property_Uplo
            priceinstance.save()
            price.save()
            houseinstance.price = priceinstance
            house_instance=house.save()
            for amenity in house_instance.amenities.all():
                house_instance.amenities.add(amenity)
                house_instance.save()

            return render(request,'hostupload/done.html')

    else:
        house = HouseForm()
        price = Pricing_HouseForm()
        return render(request,'hostupload/house.html',{'house':house,'price':price})



def UploadFormview(request):

    if request.method=='POST':
        upload = UploadForm(data=request.POST)
        address = AddressForm(data=request.POST)

        if upload.is_valid() and address.is_valid() :
            form = upload.save(commit=False)
            form.pr_type = upload.cleaned_data['pr_type']
            form.user = request.user
            add = address.save()
            form.address = add
            form.save()
            request.session['property'] = form.id
            if upload.cleaned_data['pr_type']==1:
                return redirect('/host_upload/hostel/')
            else:
                return redirect('/host_upload/house/')

        else:
            print(user_info.errors,user_profile.errors)
    else:

        upload = UploadForm()
        address = AddressForm()

    return render(request,'hostupload/upload-main.html',{'upload':upload,'address':address})
