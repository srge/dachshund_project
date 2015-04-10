from django.conf.urls import patterns, url
from comparisons import views

urlpatterns = patterns(
    '',
    url(r'^results/', views.get_results, name='results'),
    url(r'^$', views.home_page, name='home'),
)
