from django.conf.urls import url, handler404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import logout_then_login

from . import views

handler404 = 'adais.views.page_not_found'

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^restaurant/(?P<url_id>\d+)/$', views.restaurant, name='restaurant'),
  url(r'^day/(?P<url_id>\d{1})/$', views.day, name='day'),
  url(r'^dashboard/$', views.dashboard, name='dashboard'),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^signup/complete/$', views.signup_complete, name="signup_complete"),
  url(r'^login/$', views.user_login, name='login'),
  url(r'^logout/$', lambda request: logout_then_login(request, "/"), name="logout"),
  url(r'^addDeal/$', views.addDeal, name='addDeal'),
]
