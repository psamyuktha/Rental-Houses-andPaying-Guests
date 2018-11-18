from django.shortcuts import render
from django.http import HttpResponse
from .models import variables,Amenities,Property_Type,Address,Property_Upload,Pricing_House,House,Pricing_Hostel,Hostel,Booking_House,Booking_Hostel
def plz4(request):
    p=[]
    print(k)
    for i in range(0,len(k)):
        x = k
        print(x)
        s=','
        n1=[]
        n1.append(x[i].address.street)
        n1.append(x[i].address.city)
        n1.append(x[i].address.state)
        n2=s.join(n1)
        p.append(n2)
    print(p)
    sel={
    "selected":p
    }
    return render(request,'basic/maps.html',context=sel)
def plz2(request):
    return render(request,'basic/block.html')
def plz1(request):
    return render(request,'basic/iframe.html')

def plz(request):
    if request.method=="POST":
        low=500
        medium=1000
        high=15000
        housetype = request.POST.get('housetype')
        pricerange = request.POST.get('pricerange')
        if housetype!="none" :
            if housetype=="house":
                house = House.objects.all()
                l=fil(house)
                sel={"selected" : l}
                return render(request,'basic/home.html',context=sel)
            if housetype=="hostel":
                hostel = Hostel.objects.all()
                l=fil1(hostel)
                sel={"selected" : l}
                return render(request,'basic/home.html',context=sel)
    house = House.objects.all()
    hostel=Hostel.objects.all()
    housel=fil(house)
    hostell=fil1(hostel)
    l=housel+hostell
    global k
    k=l
    sel={"selected" : l}
    return render(request,'basic/home.html',context=sel)
def fil(house):
    navya='2018-11-17'
    guest=4
    a=int(navya[0:4])
    a1=int(navya[5:7])
    a2=int(navya[8:10])
    sai = '2018-11-20'
    b=int(sai[0:4])
    b1=int(sai[5:7])
    b2=int(sai[8:10])
    l=[]
    for i in range(0,len(house)):
        bhouse=Booking_House.objects.filter(Pr_id = house[i].pr_id)
        if len(bhouse) != 0:
            single=house[i].single_a
            singlew=house[i].single_wa
            double=house[i].double_a
            doublew=house[i].double_wa
            triple=house[i].triple_a
            triplew=house[i].triple_wa
            bsingle=0
            bsinglew=0
            bdouble=0
            bdoublew=0
            btriple=0
            btriplew=0
            for j in range(0,len(bhouse)):
                bcheckind=bhouse[j].check_in
                bcheckoutd=bhouse[j].check_out
                bcheckin = bcheckind.isoformat()
                bcheckout = bcheckoutd.isoformat()
                c=int(bcheckin[0:4])
                c1=int(bcheckin[5:7])
                c2=int(bcheckin[8:10])
                d=int(bcheckout[0:4])
                d1=int(bcheckout[5:7])
                d2=int(bcheckout[8:10])
                #if navya<bcheckin and sai<bcheckout:
                if a2<c2 and a1<=c1 and a<=c:
                    if b2<d2 and b1<=d1 and b<=d:
                        bsingle+=bhouse[j].single_a
                        bsinglew+=bhouse[j].single_wa
                        bdouble+=bhouse[j].double_a
                        bdoublew+=bhouse[j].double_wa
                        btriple+=bhouse[j].triple_a
                        btriplew+=bhouse[j].triple_wa
                #if navya>bcheckin and sai<bcheckout:
                if a2>c2 and a1>=c1 and a>=c:
                    if b2<d2 and b1<=d1 and b<=d:
                        bsingle+=bhouse[j].single_a
                        bsinglew+=bhouse[j].single_wa
                        bdouble+=bhouse[j].double_a
                        bdoublew+=bhouse[j].double_wa
                        btriple+=bhouse[j].triple_a
                        btriplew+=bhouse[j].triple_wa
                #if navya>bcheckin and sai>bcheckout:
                if a2>c2 and a1>=c1 and a>=c:
                    if b2>d2 and b1>=d1 and b>=d:
                        bsingle+=bhouse[j].single_a
                        bsinglew+=bhouse[j].single_wa
                        bdouble+=bhouse[j].double_a
                        bdoublew+=bhouse[j].double_wa
                        btriple+=bhouse[j].triple_a
                        btriplew+=bhouse[j].triple_wa
                if a2<=c2 and a1<=c1 and a<=c:
                    if b2<=d2 and b1<=d1 and b<=d:
                        bsingle=bsingle+bhouse[j].single_a
                        bsinglew+=bhouse[j].single_wa
                        bdouble+=bhouse[j].double_a
                        bdoublew+=bhouse[j].double_wa
                        btriple+=bhouse[j].triple_a
                        btriplew+=bhouse[j].triple_wa
        nsingle=single-bsingle
        nsinglew=singlew-bsinglew
        ndouble=double-bdouble
        ndoublew=doublew-bdoublew
        ntriple=triple-btriple
        ntriplew=triplew-btriplew
        total=nsingle+nsinglew+2*ndouble+2*ndoublew+3*ntriple+3*ntriplew
        print(total)
        if total >= guest:
            l.append(house[i].pr_id)
    return l
def fil1(hostel):
    navya='2018-11-17'
    guest=4
    a=int(navya[0:4])
    a1=int(navya[5:7])
    a2=int(navya[8:10])
    sai = '2018-11-20'
    b=int(sai[0:4])
    b1=int(sai[5:7])
    b2=int(sai[8:10])
    l=[]
    for i in range(0,len(hostel)):
        bhostel=Booking_hostel.objects.filter(Pr_id = house[i].pr_id)
        if len(bhostel) != 0:
            single=hostel[i].single_a
            singlew=hostel[i].single_wa
            double=hostel[i].double_a
            doublew=hostel[i].double_wa
            triple=hostel[i].triple_a
            triplew=hostel[i].triple_wa
            bsingle=0
            bsinglew=0
            bdouble=0
            bdoublew=0
            btriple=0
            btriplew=0
            for j in range(0,len(bhouse)):
                bcheckind=bhostel[j].check_in
                bcheckoutd=bostel[j].check_out
                bcheckin = bcheckind.isoformat()
                bcheckout = bcheckoutd.isoformat()
                c=int(bcheckin[0:4])
                c1=int(bcheckin[5:7])
                c2=int(bcheckin[8:10])
                d=int(bcheckout[0:4])
                d1=int(bcheckout[5:7])
                d2=int(bcheckout[8:10])
                #if navya<bcheckin and sai<bcheckout:
                if a2<c2 and a1<=c1 and a<=c:
                    if b2<d2 and b1<=d1 and b<=d:
                        bsingle+=bhostel[j].single_a
                        bsinglew+=bhostel[j].single_wa
                        bdouble+=bhostel[j].double_a
                        bdoublew+=bhostel[j].double_wa
                        btriple+=bhostel[j].triple_a
                        btriplew+=bhostel[j].triple_wa
                #if navya>bcheckin and sai<bcheckout:
                if a2>c2 and a1>=c1 and a>=c:
                    if b2<d2 and b1<=d1 and b<=d:
                        bsingle+=bhostel[j].single_a
                        bsinglew+=bhostel[j].single_wa
                        bdouble+=bhostel[j].double_a
                        bdoublew+=bhostel[j].double_wa
                        btriple+=bhostel[j].triple_a
                        btriplew+=bhostel[j].triple_wa
                #if navya>bcheckin and sai>bcheckout:
                if a2>c2 and a1>=c1 and a>=c:
                    if b2>d2 and b1>=d1 and b>=d:
                        bsingle+=bhostel[j].single_a
                        bsinglew+=bhostel[j].single_wa
                        bdouble+=bhostel[j].double_a
                        bdoublew+=bhostel[j].double_wa
                        btriple+=bhostel[j].triple_a
                        btriplew+=bhostel[j].triple_wa
                if a2<=c2 and a1<=c1 and a<=c:
                    if b2<=d2 and b1<=d1 and b<=d:
                        bsingle+=bhostel[j].single_a
                        bsinglew+=bhostel[j].single_wa
                        bdouble+=bhostel[j].double_a
                        bdoublew+=bhostel[j].double_wa
                        btriple+=bhostel[j].triple_a
                        btriplew+=bhostel[j].triple_wa
        nsingle=single-bsingle
        nsinglew=singlew-bsinglew
        ndouble=double-bdouble
        ndoublew=doublew-bdoublew
        ntriple=triple-btriple
        ntriplew=triplew-btriplew
        total=nsingle+nsinglew+2*ndouble+2*ndoublew+3*ntriple+3*ntriplew
        if total >= guest:
            l.append(hostel[i].pr_id)
    return l
