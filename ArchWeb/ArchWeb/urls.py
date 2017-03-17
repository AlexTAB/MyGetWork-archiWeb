"""ArchWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static 
from django.views.static import serve
from main import views
import os

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^home/gallery/$', views.gallery, name = 'gallery'),
    #url(r'^home/gallery/', views.gallery, name = 'gallery'),
    url(r'^home/login/', RedirectView.as_view(pattern_name='login'), name = 'to_login'),
    url(r'^login/', views.login, name = 'login'),
    url(r'^login/passwordreset/', RedirectView.as_view(pattern_name='passwordreset')),
    url(r'^inscription/', views.test, name = 'inscription'),
    url(r'^home/inscription', RedirectView.as_view(pattern_name='inscription'), name='to_inscription'),
    url(r'^passwordreset/$', views.passwordreset, name='passwordreset'),
    url(r'^changepassword/(?P<name>\w+)/', views.changepassword, name='changepassword'),
    url(r'^passwordreset/changepassword/(?P<name>\w+)/', 
        RedirectView.as_view(pattern_name='changepassword')),
    url(r'^article_index/', views.IndexView.as_view(), name='article'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', views.ArchiveView.as_view(), name='archive'),
    url(r'^write/$', views.write, name='write'),


    url(r'video/$', views.Video, name='video'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}, name='image'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

