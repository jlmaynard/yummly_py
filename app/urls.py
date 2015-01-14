#Here are all of Pyum's URLS.
from django.conf.urls import patterns, url
from django.contrib import admin

from app import views


admin.autodiscover()

urlpatterns = patterns('',
                       #User types nothing, go to home
                       url(r'^$', views.home, name='home'),
                       #Register
                       url(r'^register/$', views.register, name='register'),
                       #Search Recipes
                       url(r'^search_recipes/$', views.search_recipes, name='search_recipes'),
                       #Log in
                       url(r'^login/$', views.user_login, name='login'),
                       #Log Out
                       url(r'^logout/$', views.user_logout, name='logout'),
                       #Home
                       url(r'^home/$', views.home, name='home'),
                       #Profile
                       url(r'^profile/$', views.profile, name='profile'),
                       #About
                       url(r'^about/$', views.about, name='about'),
                       #Static files, get django to serve em.
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve'), )
