from django.conf.urls import url, include

from .views import myview, template, Index

urlpatterns = [
	url(r'^pdf/$', myview, name='pdf'),
	url(r'^template/$', template.as_view(), name='template'),
	url(r'^$', Index.as_view(), name='index'),
	
]