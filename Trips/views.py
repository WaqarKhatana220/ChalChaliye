from django.shortcuts import render, redirect
import datetime
from .models import Trip
def Basics(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Title = request.POST.get('Title', '')
            Destination = request.POST.get('Destination', '')
            Sdate = request.POST.get('Sdate', '')
            Edate = request.POST.get('Edate', '')
            Pic = request.POST.get('img', '')
            request.session['Title'] = Title
            request.session['Destination'] = Destination
            request.session['Sdate'] = Sdate
            request.session['Edate'] = Edate
            request.session['pic']=Pic
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
                USER=request.user
                User=USER.username.split(" ")
                if(len(User)==1):
                    User=User[0][0]+User[0][-1]
                else:
                    User=User[0][0]+User[1][0]
                return render(request, 'Basics.html',{'user':User,'Title':t,'Destination':d,'Sdate':s,'Edate':e,'Pic':p})
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
                    print(Sdate,Edate,title,Included)
                    trip=Trip(Title=title,Destination=destination,Sdate=Sdate,
                    Edate=Edate,picture=pic,About_Trip=About_Trip,Included=Included,NotIncluded=NotIncluded,
                    time=time,city=city,address=address,itinerary=itinerary,price=price,DeadLine=DeadLine,
                    discount=discount,Gsize=int(Gsize),Amount=Amount)
                    trip.save()
                    print("Saved")
                    return redirect("HomePage")
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
            trip=Trip.objects.filter(Destination=to,city=fro)
            return render(request,'Trips.html',{'Trips':trip,'user':User})
        else:
            trip=Trip.objects.all()
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
        return render(request,'MyTrips.html',{'user':User})
    else:
        return redirect('SignIn')
