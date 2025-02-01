from django.shortcuts import render, redirect
import datetime
from .models import Trip,Booking
from login.models import Profile1
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
def Basics(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Title = request.POST.get('Title', '')
            Destination = request.POST.get('Destination', '')
            Sdate = request.POST.get('Sdate', '')
            Edate = request.POST.get('Edate', '')
            print(len(request.FILES))
            for i in request.FILES:
                print("i",i)
            # image=request.FILES.get('img','')
            # fs=FileSystemStorage()
            # # print(image.name)
            # # filname=fs.save(image,image)
            # # url=fs.url(filname)
            # print(image)
            # print(image)
            # # print(url)
            # # print(url)
            pe=request.POST.get('people', '')
            request.session['Title'] = Title
            request.session['Destination'] = Destination
            request.session['Sdate'] = Sdate
            request.session['Edate'] = Edate
            request.session['pic']=None
            request.session['people']=pe
            # name=request.session.pop('Title')
            # print(name)
            return redirect('Description')
        else:
            if(request.session.has_key('Title')):
                t=request.session.pop('Title')
                d=request.session.pop('Destination')
                s=request.session.pop('Sdate')
                e=request.session.pop('Edate')
                p=request.session.pop('pic')
                people=request.session.pop('people')
                USER=request.user
                User=USER.username.split(" ")
                if(len(User)==1):
                    User=User[0][0]+User[0][-1]
                else:
                    User=User[0][0]+User[1][0]
                return render(request, 'Basics.html',{'user':User,'Title':t,'Destination':d,'Sdate':s,'Edate':e,'Pic':p,'people':people})
            USER=request.user
            User=USER.username.split(" ")
            print(type(USER.username))
            if(len(User)==1):
                User=User[0][0]+User[0][-1]
            else:
                User=User[0][0]+User[1][0]
            print(request.user.is_authenticated)
            return render(request, 'Basics.html',{'user':User})
    else:
         return redirect('SignIn')


def Description(request):
    if request.method == "POST":
        About_Trip = request.POST.get('aboutTrip', '')
        Included = request.POST.get('included', '')
        NotIncluded = request.POST.get('notIncluded', '')
        print(type(request.session))
            # print("boom")
        if(request.session.has_key('Title')):
            # print(request.session.pop('Title'),request.session.pop('Destination'),request.session.pop('Sdate'),request.session.pop('Edate'))
            request.session['About_Trip'] = About_Trip
            request.session['Included'] = Included
            request.session['NotIncluded'] = NotIncluded
            return redirect('Iterations')
        else:
            return redirect('Basics')
    if not(request.session.has_key('Title')):
        return redirect("Basics")
    USER=request.user
    User=USER.username.split(" ")
    if(len(User)==1):
        User=User[0][0]+User[0][-1]
    else:
        User=User[0][0]+User[1][0]
    if(request.session.has_key('About_Trip')):
        print("\n","\n")
        a=request.session.pop('About_Trip')
        i=request.session.pop('Included')
        n=request.session.pop('NotIncluded')
        print(a,i,n)
        return render(request, 'Trip_desc.html',{'user':User,'About_Trip':a,'Included':i,'NotIncluded':n})
    return render(request, 'Trip_desc.html',{'user':User})


def Iterations(request):
    if request.method == "POST":
        time = request.POST.get('time', '')
        city = request.POST.get('city', '')
        address = request.POST.get('address', '')
        time = request.POST.get('time', '')
        itinerary = request.POST.get('itinerary', '')
        print(time, city, address)

        if (request.session.has_key('Title')):

            if(request.session.has_key('About_Trip')):

                request.session['time'] = time
                request.session['city'] = city
                request.session['address'] = address
                request.session['itinerary'] = itinerary
                return redirect('Price')
            else:

                return redirect("Description")
        else:

            return redirect("Basics")
    if not(request.session.has_key('Title')):
        return redirect("Basics")
    if not(request.session.has_key('About_Trip')):
         return redirect("Description")
    USER=request.user
    User=USER.username.split(" ")
    if(len(User)==1):
        User=User[0][0]+User[0][-1]
    else:
        User=User[0][0]+User[1][0]
    if(request.session.has_key('time')):
        t=request.session.pop('time')
        c=request.session.pop('city')
        a=request.session.pop('address')
        i=request.session.pop('itinerary')
        return render(request, 'Iterations.html',{'user':User,'time':t,'city':c,'address':a,'itinerary':i})
    return render(request, 'Iterations.html',{'user':User})


def Price(request):
    if request.method == "POST":
        price =int(request.POST.get('Price', ''))
        DeadLine = request.POST.get('bookingDeadline', '')
        discount = request.POST.get('discount', '')
        Gsize=0
        Amount=0
        if discount == "yes":
            Gsize = int(request.POST.get('groupSize', ''))
            Amount = int(request.POST.get('amount', ''))
            # print(price,DeadLine,discount,Gsize,Amount)
            print(type(Gsize),type(Amount),DeadLine)

        if(request.session.has_key('Price')):
            request.session.pop('Price')
            request.session.pop('bookingDeadline')
            name = request.session.pop('discount')
            if name == "yes":
                request.session.pop('groupSize')
                request.session.pop('amount')
        if (request.session.has_key('Title')):

            if(request.session.has_key('About_Trip')):

                if(request.session.has_key('time')):

                    title = request.session.pop('Title')
                    destination = request.session.pop('Destination')
                    Sdate = request.session.pop('Sdate')
                    Edate = request.session.pop('Edate')

                    Sdate=Sdate.split("-")
                    Sdate=datetime.date(int(Sdate[0]),int(Sdate[1]),int(Sdate[2]))

                    Edate=Edate.split("-")
                    Edate=datetime.date(int(Edate[0]),int(Edate[1]),int(Edate[2]))

                    DeadLine=DeadLine.split("-")
                    DeadLine=datetime.date(int(DeadLine[0]),int(DeadLine[1]),int(DeadLine[2]))
                    pic = request.session.pop('pic')
                    About_Trip = request.session.pop('About_Trip')
                    Included = request.session.pop('Included')
                    NotIncluded = request.session.pop('NotIncluded')
                    time = request.session.pop('time')
                    city = request.session.pop('city')
                    address = request.session.pop('address')
                    itinerary = request.session.pop('itinerary')
                    people = int(request.session.pop('people'))
                    print(Sdate,Edate,title,Included)
                    trip=Trip(user=request.user,Title=title,Destination=destination,Sdate=Sdate,
                    Edate=Edate,picture=pic,About_Trip=About_Trip,Included=Included,NotIncluded=NotIncluded,
                    time=time,city=city,address=address,itinerary=itinerary,price=price,DeadLine=DeadLine,
                    discount=discount,Gsize=int(Gsize),Amount=Amount,people=people)
                    trip.save()
                    print("Saved")
                    return redirect("Trips")
                else:
                    return redirect("Iterations")
            else:
                return redirect("Description")
        else:
            return redirect("Basics")
    if not(request.session.has_key('Title')):
        return redirect("Basics")
    if not(request.session.has_key('About_Trip')):
         return redirect("Description")
    if not(request.session.has_key('time')):
        return redirect("Iterations")
    USER=request.user
    User=USER.username.split(" ")
    if(len(User)==1):
        User=User[0][0]+User[0][-1]
    else:
        User=User[0][0]+User[1][0]
    return render(request, 'price.html',{'user':User})

def Trips(request):
    if request.user.is_authenticated:
        USER=request.user
        User=USER.username.split(" ")
        if(len(User)==1):
            User=User[0][0]+User[0][-1]
        else:
            User=User[0][0]+User[1][0]
        if request.method=="POST":
            fro =request.POST.get('from', '')
            to = request.POST.get('to', '')
            filters = {}
            if to and len(to) > 0:
                filters["Destination"] = to
            if fro and len(fro) > 0:
                filters["city"] = fro
            trip=Trip.objects.filter(**filters)
            if not trip:
                return render(request,'Trips.html',{'Trips':trip,'user':User})
            trips_list=[]
            for i in trip:
                day=((i.Edate-i.Sdate).days)
                prof=Profile1.objects.filter(user=i.user).first()
                trips_list.append([i,prof,day])

            return render(request,'Trips.html',{'Trips':trips_list,'user':User})
        else:
            tri=Trip.objects.all()
            trip=[]
            for i in tri:
                day=((i.Edate-i.Sdate).days)
                prof=Profile1.objects.filter(user=i.user).first()
                trip.append([i,prof,day])

            return render(request,'Trips.html',{'Trips':trip,'user':User})
    else:
        return redirect('SignIn')
    
def MyTrip(request):
    if request.user.is_authenticated:
        USER=request.user
        User=USER.username.split(" ")
        if(len(User)==1):
            User=User[0][0]+User[0][-1]
        else:
            User=User[0][0]+User[1][0]
        trip=Trip.objects.filter(user=USER)
        l=[]
        for i in trip:
            B=Booking.objects.filter(trip=i)
            size=0
            if len(B)!=0 :
                for j in B:
                    size=size+j.participent
            l.append([i,size])
            print(size)
        return render(request,'MyTrips.html',{'user':User,'Trips':l})
    else:
        return redirect('SignIn')
import re
def book(request,id):
    trip=Trip.objects.filter(id=id).first()
    desc= re.split(',|\n', trip.Included)
    not_included=re.split(',|\n', trip.NotIncluded)
    if(request.session.has_key('trip_id')):
        request.session.pop('trip_id')
    request.session['trip_id']=id
    print(trip)
    B=Booking.objects.filter(trip=trip)
    size=0
    if len(B)!=0 :
        for i in B:
            size=size+i.participent
    size=trip.people-size
    prof=Profile1.objects.filter(user=trip.user).first()
    pic=prof.picture
    return render(request,'book.html',{'trip':trip,'desc':desc, 'not_included': not_included, 'size':size,'pic':pic})
def ticket_book(request):
    if request.method == "POST":
        participent=request.POST.get('part', '')
        print(participent)
        user=request.user.username
        id=request.session.pop('trip_id')
        trip=Trip.objects.filter(id=id).first()
        B=Booking.objects.filter(trip=trip)
        size=0
        if len(B)!=0 :
            for i in B:
                size=size+i.participent
        if(size==trip.people):
            messages.info(request,'Trip Size full')
            return redirect('Trips')
        if(size+int(participent)>trip.people):
            messages.info(request,'Not enough Tickets')
            return redirect('Trips')
        if(request.user==trip.user):
            messages.info(request,'You cannot book the ticket, bro it this is your trip')
            return redirect('Trips')
        else:
            book1=Booking(user=user,trip=trip,participent=participent)
            book1.save()
            messages.info(request,'Ticket is booked')
        return redirect('Trips')

def trip_info(request,id):
    trip=Trip.objects.filter(id=id).first()
    B=Booking.objects.filter(trip=trip)
    size=0
    amount=1
    if len(B)!=0 :
        for i in B:
            size=size+i.participent
        if size>trip.Gsize:
            amount=trip.Amount*amount+amount
        else:
            amount=trip.price*amount+amount
    print(amount)
    k=[]
    for i in B:
        a=1
        if i.participent>i.trip.Gsize:
            a=trip.Amount*i.participent
        else:
            a=trip.price*i.participent
        print("p",i.participent,a,trip.price)
        k.append([i.user,a,i.participent,i.date])
        print(i.date)
    if(request.session.has_key('del')):
        request.session.pop('del')
    request.session['del']=id        
    return render(request,'manage.html',{'id':id,'trip':trip,'size':size,'totol1':amount,'booking':k})

def dell(request):
    if request.method == "POST": 
        id= request.session.pop('del')
        Trip.objects.filter(id=id).delete()
        return redirect('MyTrips')