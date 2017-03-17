from django import forms
from django.forms import ModelForm
from django.views.generic import ListView
from main.models import Client, Photo, Contact, Article
class InfoLoginForm(forms.Form):
	username = forms.CharField(required = True)
	pwd = forms.CharField(required=True,widget = forms.PasswordInput())
	def __init__(self, *args, **kwargs):
		super(InfoLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs = {'class':'form-control', 'placeholder':'Enter your username'}
		self.fields['pwd'].widget.attrs = {'class':'form-control', 'placeholder':'Enter your password'}

class InfoSignupForm(forms.Form):
	yourname = forms.CharField(label='Your Name',required=True)
	email = forms.EmailField(label='Your Email',help_text="example@example.fr",required=True)
	username = forms.CharField(label='Username',required=True)
	password = forms.CharField(label='Password',required=True,widget=forms.PasswordInput())
	passwordConfirm = forms.CharField(label='Password Confirm',required=True,widget=forms.PasswordInput())
	def __init__(self, *args, **kwargs):
		super(InfoSignupForm,self).__init__(*args, **kwargs)
		self.fields['yourname'].widget.attrs = {'class':'form-control',
											'placeholder':'Enter your real name '}
		#self.fields['yourname'].label.attrs['class'] = 'cols-sm-2 control-label'
		self.fields['email'].widget.attrs = {'class':'form-control',
											'placeholder':'Enter your email'}
		self.fields['username'].widget.attrs = {'class':'form-control',
											'placeholder':'Enter your username '}
		self.fields['password'].widget.attrs = {'class':'form-control',
											'placeholder':'Enter your password'}
		self.fields['passwordConfirm'].widget.attrs = {'class':'form-control',
											'placeholder':'Definit your password'}

class ClientForm(ModelForm):
	class Meta:
		model = Client
		fields = ['name','email','username']
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'username':forms.TextInput(attrs={'class':'form-control'})
		}

class PasswordChangeForm(forms.Form):
	password1= forms.CharField(required=True,widget=forms.PasswordInput())
	password2= forms.CharField(required=True,widget=forms.PasswordInput())
	def __init__(self, *args, **kwargs):
		super(PasswordChangeForm,self).__init__(*args, **kwargs)
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class PhotoForm(ModelForm):
	class Meta:
		model = Photo
		fields = ['title', 'image', 'caption']
		widgets = {
			'title' : forms.TextInput(attrs={'class':''}),
			'image' :  forms.FileInput(attrs={'style':'color: white'})
		}

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields =  '__all__'
		widgets = {
			'name_contactor' : forms.TextInput(attrs={'class':'form-control'}),
			'email_contactor' : forms.EmailInput(attrs={'class':'form-control'}),
			'message' : forms.TextInput(attrs={'class':'form-control'})
		}

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		exclude = ['user']
