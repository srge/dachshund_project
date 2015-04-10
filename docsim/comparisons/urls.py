from django.conf.urls import patterns, url
from comparisons import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home_page, name='home'),
)
