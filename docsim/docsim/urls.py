from django.conf.urls import patterns, include, url
from django.contrib import admin

from docsim import views


urlpatterns = patterns('',
    #url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('comparisons.urls')),
    url(r'^', include('comparisons.urls')),
)
