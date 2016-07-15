from django.shortcuts import render

from .functions import generarPDF

def myview(request):
	context = {'titulo' : 'Primer PDF generado con Django',
				'contenido' : 'Generado con python 3  reportlab',
                'tipo' : 'reporte'
	}
	return generarPDF('mytemplate.html', context)