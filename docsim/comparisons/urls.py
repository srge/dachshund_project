from django.conf.urls import patterns, url
from comparisons import views

urlpatterns = patterns(
    '',
    url(r'^results/', views.get_results, name='results'),
    url(r'^results/(?P<id_c>[0-9]+)/$', views.get_results, name='results_id'),
    url(r'^$', views.home_page, name='home'),
)
