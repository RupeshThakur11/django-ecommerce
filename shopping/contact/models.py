from django.db import models
import datetime

# Create your models here.

class ContactUs(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)
	message = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())

	def __unicode__(self):
		return self.email

	class Meta:
		ordering = ['-timestamp']
