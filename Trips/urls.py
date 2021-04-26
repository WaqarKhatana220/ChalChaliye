from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('Basics',views.Basics,name="Basics"),
    path('Description',views.Description,name="Description"),
    path('Iterations',views.Iterations,name="Iterations"),
    path('Price',views.Price,name="Price"),
    path('Trips',views.Trips,name="Trips"),
    path('MyTrips',views.MyTrip,name="MyTrips"),
    path('Book/<int:id>',views.book,name="Book"),
    path('ticket',views.ticket_book,name="ticket"),
    path('manage/<int:id>',views.trip_info,name='manage'),
    path('Del',views.dell,name='Del'),
]