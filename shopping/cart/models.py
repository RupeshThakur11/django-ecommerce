import datetime 

from django.db import models
from django.contrib.auth.models import User

from products.models import Product
# Create your models here.

class Cart(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	total_price = models.CharField(max_length=120, default=0)
	active=models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	products = models.ManyToManyField(Product, blank=True, null=True)

	def __unicode__(self):
		return str(self.id)
