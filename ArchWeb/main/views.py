from django.shortcuts import render
from django.http import HttpResponse

def main(request):
	text = "<h1>Hello World<h1>"
	return HttpResponse(text)
# Create your views here.

def login(request):
	user = ['nom','prenom','password','email']
	return render(request, 'inscription.html', {'user':user})