# Create your views here.
from datetime import date
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Product

def product_page(request):
	products = Product.objects.all()
	return render_to_response('products.html', {'products':products},RequestContext(request))

def product_single(request, slug):
	product = Product.objects.get(slug=slug)
	return render_to_response('product_single.html', {'product':product},RequestContext(request))

def home(request):
	return render_to_response('home.html', {},RequestContext(request))




