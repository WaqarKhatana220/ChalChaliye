import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import File
class Profile1(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address=models.CharField(max_length=500,null=True)
	phone=models.CharField(null=True,max_length=100)
	cnic=models.CharField(null=True,max_length=100)
	picture = models.ImageField(null=True,upload_to ='images/')
 
	def save(self, *args, **kwargs):
		if not self.picture:
			dummy_image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images/dummy_profile.png')
			if os.path.exists(dummy_image_path):
				with open(dummy_image_path, 'rb') as img:
					self.picture.save('dummy_profile.png', File(img), save=False)
		super().save(*args, **kwargs)
        
	def __str__(self):
		return str(self.user.username)

	def download_image(url):
		"""Downloads an image and makes sure it's verified.

		Returns a PIL Image if the image is valid, otherwise raises an exception.
		"""
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'} # More likely to get a response if server thinks you're a browser
		r = urllib2.Request(url, headers=headers)
		request = urllib2.urlopen(r, timeout=10)
		image_data = cStringIO.StringIO(request.read()) # StringIO imitates a file, needed for verification step
		img = Image.open(image_data) # Creates an instance of PIL Image class - PIL does the verification of file
		img_copy = copy.copy(img) # Verify the copied image, not original - verification requires you to open the image again after verification, but since we don't have the file saved yet we won't be able to. This is because once we read() urllib2.urlopen we can't access the response again without remaking the request (i.e. downloading the image again). Rather than do that, we duplicate the PIL Image in memory.
		if valid_img(img_copy):
			return img
		else:
			# Maybe this is not the best error handling...you might want to just provide a path to a generic image instead
			raise Exception('An invalid image was detected when attempting to save a Product!')


	def valid_img(img):
		"""Verifies that an instance of a PIL Image Class is actually an image and returns either True or False."""
		type = img.format
		if type in ('GIF', 'JPEG', 'JPG', 'PNG'):
			try:
				img.verify()
				return True
			except:
				return False
		else: return False