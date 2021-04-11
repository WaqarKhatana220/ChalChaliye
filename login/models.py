from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	CNIC=models.CharField(max_length=13)
	Picture = models.ImageField()
	def __str__(self):
		return str(self.user.username)


	
