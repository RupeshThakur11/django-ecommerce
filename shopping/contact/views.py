# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import ContactUsForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def contact(request):

	form = ContactUsForm(request.POST or None)
	if form.is_valid():
		this_form = form.save(commit=False)
		this_form.save()
		return HttpResponseRedirect ('/')

	return render_to_response('contact.html', {'form':form}, RequestContext(request))

