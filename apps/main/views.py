from django.shortcuts import render
from django.views.generic import TemplateView

from .functions import generarPDF

def myview(request):
	context = {'titulo' : 'Primer PDF generado con Django',
				'contenido' : 'Generado con python 3  reportlab',
                'tipo' : 'reporte'
	}
	return generarPDF('mytemplate.html', context)

class template(TemplateView):
    template_name = 'mytemplate.html'

class Index(TemplateView):
    template_name= 'index.html'