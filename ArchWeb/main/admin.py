from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
	fields = ['name', 'mail','username','password']

admin.site.register(User, UserAdmin)