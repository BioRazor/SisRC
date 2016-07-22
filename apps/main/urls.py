from django.conf.urls import url, include

from .views import pdfLaptop, template, Index

urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),
	url(r'^template/$', template.as_view(), name='template'),
	url(r'^pdf/(?P<pk>\d+)/$', pdfLaptop, name='pdfLaptop'),

	
]