from django.shortcuts import render
from django.views.generic import TemplateView

from .functions import generarPDF
from .models import Servicio_Tecnico_Laptop

def pdfLaptop(request, pk):
	context = Servicio_Tecnico_Laptop.objects.get(pk = pk)
	return generarPDF('pdfservicio.html', context, context, 'Laptop')

class template(TemplateView):
    template_name = 'pdfservicio.html'

class Index(TemplateView):
    template_name= 'index.html'