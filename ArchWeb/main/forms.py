from django import forms

class InfoLoginForm(forms.Form):
	username = forms.CharField(required = True)
	pwd = forms.CharField(required=True,widget = forms.PasswordInput())
	def __init__(self, *args, **kwargs):
		super(InfoLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['style'] = 'width:500px; height:auto;'
		self.fields['pwd'].widget.attrs['style'] = 'width:500px; height:auto;'

class InfoSignupForm(forms.Form):
	yourname = forms.CharField(label='Your Name',required=True)
	email = forms.EmailField(label='Your Email',help_text="example@example.fr",required=True)
	username = forms.CharField(label='Username',required=True)
	password = forms.CharField(label='Password',required=True,widget=forms.PasswordInput())
	passwordConfirm = forms.CharField(label='Password Confirm',required=True,widget=forms.PasswordInput())
	def __init__(self, *args, **kwargs):
		super(InfoSignupForm,self).__init__(*args, **kwargs)
		self.fields['yourname'].widget.attrs['style'] = 'width:280px; height:auto;'
		#self.fields['yourname'].label.attrs['class'] = 'cols-sm-2 control-label'
		self.fields['email'].widget.attrs['style'] = 'width:280px; height:auto;'
		self.fields['username'].widget.attrs['style'] = 'width:280px; height:auto;'
		self.fields['password'].widget.attrs['style'] = 'width:280px; height:auto;'
		self.fields['passwordConfirm'].widget.attrs['style'] = 'width:280px; height:auto;'