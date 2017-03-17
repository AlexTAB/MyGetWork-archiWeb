from django.contrib import admin

# Register your models here.
from .models import Client, Photo, Category, Article, Tag

class PhotoInline(admin.StackedInline):
	model = Photo

class UserAdmin(admin.ModelAdmin):
	fields = ['name', 'email','username','password']
	list_display = ('name','email','username','password')
	inlines = [PhotoInline]



admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Client, UserAdmin)
admin.site.register(Photo)
