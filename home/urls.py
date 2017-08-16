from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^createuser', views.createuser,name='createuser'),
	url(r'^login', views.login, name='login'),
	url(r'^ladingpage',views.landingpage, name='landingpage'),
]

urlpatterns += staticfiles_urlpatterns()