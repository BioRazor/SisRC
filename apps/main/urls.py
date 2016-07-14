from django.conf.urls import url, include

from .views import myview

urlpatterns = [
	url(r'^pdf/', myview, name='pdf')
]