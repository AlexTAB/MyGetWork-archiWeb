from django.db import models
from django.core.urlresolvers import reverse
from collections import defaultdict

import datetime
# Create your models here.
class Client(models.Model):
	name = models.CharField("Name", max_length = 30)
	email = models.EmailField("Email", max_length = 80)
	username = models.CharField("Username", max_length = 20)
	password = models.CharField("Password", max_length = 20)

	primary = ['name','ID']
	def __str__(self):
		return self.name
	@models.permalink

	def get_absolute_url(self):
		return ('item_detail', None, {'objetc_id':self.id})


class Photo(models.Model):
	item = models.ForeignKey(Client)
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos')
	caption = models.CharField(max_length=250, blank=True)

	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title

	@models.permalink

	def get_absolute_url(self):
		return ('photo_detail', None, {'object_id':self.id})

class Contact(models.Model):
	name_contactor = models.CharField("Name_Contactor",max_length=30)
	email_contactor = models.EmailField("Email_Contactor")
	message = models.TextField("Message")
	created_time = models.DateTimeField("Time Created", auto_now_add = True)

	class Meta:
		ordering = ['created_time']

	def __str__(self):
		return self.message

class ArticleManage(models.Manager):
	def archive(self):
		date_list = Article.objects.datetimes('created_time','month', order='DESC')
		date_dict = defaultdict(list)
		for d in date_list:
			date_dict[d.year].append(d.month)
		return sorted(date_dict.items(), reverse=True)

class Article(models.Model):
	

	STATUS_CHOICES = (
		('d', 'Draft'),
		('p', 'Published'),
	)

	objects = ArticleManage()

	title = models.CharField('Title', max_length=70)
	body = models.TextField('Body')
	created_time = models.DateTimeField('Created Time', auto_now_add=True)
	last_modified_time = models.DateTimeField('Last Modified Time', auto_now=True)
	status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES)
	views = models.PositiveIntegerField('Views', default = 0)
	likes = models.PositiveIntegerField('Likes', default = 0)
	topped = models.BooleanField('Topped', default=False)

	category = models.ForeignKey('Category', verbose_name='Classification',
		null=True, on_delete=models.SET_NULL)
	user = models.ForeignKey('Client')
	tags = models.ManyToManyField('Tag', verbose_name="ensemble", blank=True)
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-last_modified_time']

class Category(models.Model):
	name = models.CharField('Category', max_length=20)
	created_time = models.DateTimeField('Created Time', auto_now_add=True)
	last_modified_time = models.DateTimeField('Last Modified Time', auto_now=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name=models.CharField('Name Tag', max_length=20)
	created_time=models.DateTimeField('Created Time', auto_now_add=True)
	last_modified_time=models.DateTimeField('Last Modified Time', auto_now=True)
	def __str__(self):
		return self.name














	