from django.db import models

# Create your models here.
class Trip(models.Model):
    user=models.CharField(max_length=32,null=True)
    Title=models.CharField(max_length=32,null=True)
    Destination=models.CharField(max_length=32,null=True)
    picture=models.ImageField(upload_to ='uploads/')
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
    def __str__(self):
        return self.Title
