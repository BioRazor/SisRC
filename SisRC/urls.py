
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.main.urls', namespace='principal')),
    url(r'^cliente/', include('apps.cliente.urls', namespace='clientes')),
    url(r'^pc/', include('apps.pc.urls', namespace='pc'))
]
