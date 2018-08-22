from django.conf.urls import url
from form.views import HomeView
from . import views

urlpatterns = [
	url(r'^$', HomeView.get, name='home'),
	url(r'^success/$', views.success, name='success'),
    url(r'^plot/$', views.plot, name='plot'),
	]