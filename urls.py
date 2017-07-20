from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^process', views.process, name='process'),
	url(r'^restart', views.clear, name='restart')
]

