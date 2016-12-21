# top level DJANGOBOOK views

from django.shortcuts import render
from djangobook.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.http import HttpResponse
import operator

def display_meta(request):
	values = sorted(request.META.items(),key = operator.itemgetter(0))
	#values.sort()
	html = []
	for k,v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def hello(request):
	return HttpResponse("Hello, world!")

def contact(request):
	if request.method != 'POST':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],	
				cd.get('email','noreply@example.com'),
				['siteowner@example.com']			
			)
			return HttpResponseRedirect('/contact/thanks/')
	return render(request,'contact_form.html',{'form':form})