from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Trip(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Title=models.CharField(max_length=32,null=True)
    Destination=models.CharField(max_length=32,null=True)
    picture=models.ImageField(upload_to ='images/')
    Sdate=models.DateField()
    Edate=models.DateField()
    About_Trip=models.CharField(max_length=100,null=True)
    Included=models.CharField(max_length=100,null=True)
    NotIncluded=models.CharField(max_length=100,null=True)
    time=models.CharField(max_length=32,null=True)
    city=models.CharField(max_length=32,null=True)
    address=models.CharField(max_length=100,null=True)
    itinerary=models.CharField(max_length=100,null=True)
    price=models.IntegerField()
    DeadLine=models.DateField()
    discount=models.CharField(max_length=32)
    Gsize=models.IntegerField()
    Amount=models.IntegerField()
    people=models.IntegerField(null=True)
    def __str__(self):
        return self.Title
    
class Booking(models.Model):
    user = models.CharField(max_length=32,null=True)
    trip=models.ForeignKey(Trip,on_delete=models.CASCADE,null=True)
    participent=models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.trip.Title