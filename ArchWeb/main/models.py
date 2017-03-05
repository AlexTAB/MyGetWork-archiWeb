from django.db import models

# Create your models here.
class Client(models.Model):
	name = models.CharField("Name", max_length = 30)
	mail = models.CharField("Email", max_length = 80)
	username = models.CharField("Username", max_length = 20)
	password = models.CharField("Password", max_length = 20)

	def __str__(self):
		return name

