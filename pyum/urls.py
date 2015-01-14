from django.conf.urls import patterns, include, url

from django.contrib import admin

#auto discover any admin urls
admin.autodiscover()

#This will basically direct any urls after the domain.
#App - into pyum
#Pyum - into pyum again
#admin - into the built-in admin site.
urlpatterns = patterns('',
                       url(r'^$', include('app.urls')),
                       url(r'^pyum/', include('app.urls')),
                       url(r'^app/', include('app.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
