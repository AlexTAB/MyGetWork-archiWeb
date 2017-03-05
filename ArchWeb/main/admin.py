from django.contrib import admin

# Register your models here.
from .models import Client

class UserAdmin(admin.ModelAdmin):
	fields = ['name', 'mail','username','password']

admin.site.register(Client, UserAdmin)