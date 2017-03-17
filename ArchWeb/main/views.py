from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import *
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from main.forms import *
from main.models import Client, Category, Article, Tag

import random
import json
import markdown2

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
					return HttpResponseRedirect("/home/")
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

def createcode():
	_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
	_upper_cases = _letter_cases.upper()  # 大写字母
	_numbers = ''.join(map(str, range(3, 10)))  # 数字
	init_chars = ''.join((_letter_cases, _upper_cases, _numbers))

	return random.sample(init_chars, 4)

def passwordreset(req):
	error = ''
	codecheck=''
	_realname=''
	if req.method == 'POST':
		formReset = ClientForm(req.POST)
		if formReset.is_valid():
			_realname = formReset.cleaned_data['name']
			_email = formReset.cleaned_data['email']
			_username = formReset.cleaned_data['username']

			try:
				Client.objects.get(name=_realname, email=_email, username=_username)
				codecheck=''.join(createcode())
				html_text = "Your code reset : <span style='color:red'> "+codecheck+"</span>"
				text = "Hello\n" +html_text
				subject = "Password Reset"
				print(''.join(codecheck))
				send_mail(subject, text, '123weibinjizhu@gmail.com',[_email])	
			except ObjectDoesNotExist:
				error = 'erreur of name or email or username'
			except BadHeaderError:
				error = 'erreur of bad header'
	else:
		formReset = ClientForm()
	return render(req, "passwordReset.html",{"formReset":formReset,
									"error":error,
									"error1":formReset.errors,
									'codecheck':json.dumps(codecheck),
									"nameclient":json.dumps(_realname)})	
def changepassword(req, name):
	error=''
	if req.method == 'POST':
		form = PasswordChangeForm(req.POST)
		if form.is_valid():
			password1=form.cleaned_data['password1']
			password2=form.cleaned_data['password2']
			print(password2+'|'+password1)
			try:
				user = Client.objects.get(name=name)
				if password1==password2:
					user.password = password1
			except ObjectDoesNotExist:
				error = "error of system"
			return HttpResponseRedirect('/home/')
		else:
			error = "Different Password"

	else:
		form = PasswordChangeForm()
	return render(req, 'changepassword.html', {'form':form,
										'error':error})

def home(req):
	return render(req, 'home.html')

def picture(req, _name_):
	error = ''
	if _name_:
		if req.method == 'POST':
			formPhoto = PhotoForm(req.POST, req.FILES)
			if formPhoto.is_valid():
				_title_ = formPhoto.cleaned_data['title']
				_image_ = formPhoto.cleaned_data['image']
				_caption_ = formPhoto.cleaned_data['caption']
				try:
					i = Client.objects.get(name=_name_)
					Photo.objects.create(item=i,title=_title_, image=_image_, caption=_caption_)
				except ObjectDoesNotExist:
					error = 'Please sign in'
				return HttpResponse('Good job')
		else:
			formPhoto = PhotoForm()
			print('pas ok'+req.method)
	else:
		error = 'Please sign in'
	return render(req, 'picture.html', {
		'error':error,
		'formPhoto':formPhoto
		})

def gallery(req):
	error = ''
	#if _name_:
	if req.method == 'POST':
		formPhoto = PhotoForm(req.POST, req.FILES)
		if formPhoto.is_valid():
			_title_ = formPhoto.cleaned_data['title']
			_image_ = formPhoto.cleaned_data['image']
			_caption_ = formPhoto.cleaned_data['caption']
			try:
				i = Client.objects.get(name=_name_)
				Photo.objects.create(item=i,title=_title_, image=_image_, caption=_caption_)
			except ObjectDoesNotExist:
				error = 'Please sign in'
			return HttpResponse('Good job')
	else:
		formPhoto = PhotoForm()
		print('pas ok'+req.method)
	#else:
	#	error = 'Please sign in'
	return render(req, 'gallery.html', {
		'error':error,
		'formPhoto':formPhoto
		})


class IndexView(ListView):
	template_name = "Article/article.html"
	context_object_name = "article_list"

	def get_queryset(self):
		article_list = Article.objects.filter(status='p')

		for article in article_list:
			article.body = markdown2.markdown(article.body, )

		return article_list

	def get_context_data(self, **kwargs):
		kwargs['category_list'] = Category.objects.all()
		kwargs['date_archive'] = Article.objects.archive()
		kwargs['tag_list'] = Tag.objects.all().order_by('name')
		return super(IndexView, self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'Article/detail.html'

	context_object_name='article'
	print("detailview")
	pk_url_kwarg = 'article_id'

	def get_object(self):
		article=super(ArticleDetailView, self).get_object()
		article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
		return article


class CategoryView(ListView):
	template_name='article/article.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
		for article in article_list:
			article.body= markdown2.markdown(article.body)
		return article_list

	def get_context_data(self, **kwargs):
		kwargs['category_list'] = Category.objects.all().order_by('name')
		return super(CategoryView, self).get_context_data(**kwargs)

class TagView(ListView):
	template_name='article/article.html'
	context_object_name='article_list'

	def get_queryset(self):
		article_list = Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
		for article in article_list :
			article.body = markdown2.markdown(article.body)
		return article_list

	def get_context_data(self, **kwargs):
		kwargs['tag_list'] = Tag.objects.all().order_by('name')
		return super(TagView, self).get_context_data(**kwargs)


class ArchiveView(ListView):
	template_name = 'Article/article.html'
	context_object_name = 'article_list'
	def get_queryset(self):
		year = int(self.kwargs['year'])
		month = int(self.kwargs['month'])

		article_list=Article.objects.filter(created_time__year=year, created_time__month=month)
		for article in article_list:
			article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'],)
		return article_list

	def get_context_data(self, **kwargs):
		kwargs['tag_list'] = Tag.objects.all().order_by('name')
		return super(ArchiveView, self).get_context_data(**kwargs)

def write(req):
	if req.method == 'POST':
		article_form = ArticleForm(req.POST)
		if article_form.is_valid():
			article = article_form.save(commit=False)
			article.user = req.user
			article.save()
			form.save_m2m()
	else:
		article_form = ArticleForm()
	return render(req, 'Article/write.html', {'article_form':article_form, 'current_user':req.user})

def Video(req):
	return render_to_response('video.html')





























