from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Client
from django.core.exceptions import *
from django.template.loader import render_to_string

from main.forms import InfoLoginForm, InfoSignupForm

def main(request):
	text = "<h1>Hello World</h1>"
	return HttpResponse(text)
# Create your views here.

def login(request):
	res = ""
	if request.method == 'POST':
		form = InfoLoginForm(request.POST)
		if form.is_valid():
			user= form.cleaned_data['username']
			password = form.cleaned_data['pwd']
			try: 
				client = Client.objects.get(username = user)
				if password == client.password:
					return HttpResponse("well done")
				else:
					res = "incorrect password"
			except ObjectDoesNotExist:
				res = "No username"
	else:
		form = InfoLoginForm()
	return render(request, 'login.html',{'form':form, 'res':res})

def test(request):
	resSignup = ""
	if request.method == 'POST':
		formSignup = InfoSignupForm(request.POST)
		#formSignup['yourname'].label_tag(attrs={'class':'cols-sm-2 control-label'})
		if formSignup.is_valid():
			yourname = formSignup.cleaned_data['yourname']
			email = formSignup.cleaned_data['email']
			username_ = formSignup.cleaned_data['username']
			password1 = formSignup.cleaned_data['password']
			password2 = formSignup.cleaned_data['passwordConfirm']
			if password2 == password1:
				Client.objects.create(
					name=yourname,
					mail=email,
					username=username_,
					password=password1
					)
				return HttpResponseRedirect('/main')
			else:
				resSignup="different password for two times"
		else:
			resSignup="failed"

	else:
		formSignup = InfoSignupForm()
	return render(request, 'inscription.html',{'formSignup':formSignup, 'resSignup':resSignup})










