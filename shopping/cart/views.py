from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

from models import Cart
from products.models import Product

def add(request, slug):
	product_add = Product.objects.get(slug=slug)
	request.session.set_expiry(60)
	try:
		active = request.session['cart']
	except:
		request.session['cart']='Empty'
	if request.session['cart'] != 'Empty':
		cart = request.session['cart']
		update_cart = Cart.objects.get(id=cart)
		update_cart.products.add(product_add)
		update_cart.save()
		request.session['total_items']=len(update_cart.products.all())

	else:
		new_cart = Cart()
		new_cart.save()
		new_cart.products.add(product_add)
		request.session['cart']=new_cart.id
		request.session['total_items'] = len(new_cart.products.all())

	return HttpResponseRedirect("/products/%s" %(slug))

def viewcart(request):
	try:
		cart_id= request.session['cart']
		cart_exists = Cart.objects.get(id=cart_id)
	except:
		cart_exists = False
		try:
			request.session['total_items'] == 0
		except:
			pass
	if cart_exists == False or cart_exists.active == False:
		message = "your cart is empty"
	if cart_exists and cart_exists.active:
		cart = cart_exists

	return render_to_response('viewcart.html', locals(), RequestContext(request))

def deleteCart(request):
	try:
		cart_id = request.session['cart']
		cart = Cart.objects.get(id=cart_id)
	except:
		cart = False
	if cart:
		deactivate = Cart.objects.get(id=cart_id)
		deactivate.active = False
		deactivate.save()
		request.session['total_items'] = 0
	return HttpResponseRedirect('/cart/')


