import os
from django.db import models
from django.contrib.auth.models import User

from django.core.files import File
from django.conf import settings

# Create your models here.
class Trip(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Title=models.CharField(max_length=255,null=True, blank=True)
    Destination=models.CharField(max_length=32,null=True, blank=True)
    picture=models.ImageField(upload_to ='images/', null=True, blank=True)
    Sdate=models.DateField()
    Edate=models.DateField()
    About_Trip=models.TextField(null=True, blank=True)
    Included=models.TextField(null=True, blank=True)
    NotIncluded=models.TextField(null=True, blank=True)
    time=models.CharField(max_length=32,null=True, blank=True)
    city=models.CharField(max_length=32,null=True, blank=True)
    address=models.CharField(max_length=100,null=True, blank=True)
    itinerary=models.CharField(max_length=100,null=True, blank=True)
    price=models.IntegerField()
    DeadLine=models.DateField()
    discount=models.CharField(max_length=32)
    Gsize=models.IntegerField(null=True, blank=True)
    Amount=models.IntegerField()
    people=models.IntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.picture:
            dummy_image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images/dummy_landscape.jpg')
            if os.path.exists(dummy_image_path):
                with open(dummy_image_path, 'rb') as img:
                    self.picture.save('dummy_landscape.jpg', File(img), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Title
    
class Booking(models.Model):
    user = models.CharField(max_length=32,null=True)
    trip=models.ForeignKey(Trip,on_delete=models.CASCADE,null=True)
    participent=models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.trip.Title