#Para python 3
try:
	import io
#para python 2
except ImportError:
	import cStringIO as StringIO

from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

from .models import Tecnico
from apps.cliente.models import Cliente
from apps.pc.models import Desktop, Laptop

def generarPDF(template_src, context_dict, nombre, tipo):
	if not nombre:
		nombre = 'reporte'
	template = get_template(template_src)
	#.__dict__ para hacer del objeto un diccionario
	context = context_dict.__dict__
	#Como no guarda el objeto tecnico, se obtiene de acuerdo al id (Que si muestra)
	tecnico = Tecnico.objects.get(id = context['tecnico_id'])
	#Se asigna en un nuevo campo el tecnico
	context['tecnico'] = tecnico
	cliente = Cliente.objects.get(id= context['cliente_id'])
	context['cliente'] = cliente
	
	if tipo == 'Laptop':
		pc = Laptop.objects.get(id=context['pc_id'])
		context['laptop'] = pc
	else:
		pc = Desktop.objects.get(id=context['pc_id'])
		context['pc'] = pc
		
	context['servicios'] = context_dict.servicios.all()
	html  = template.render(context)
	
	try:
		result = io.BytesIO()
		pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
	except ImportError:
		result = StringIO.StringIO()
		pdf = pias.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)

	if not pdf.err:
		response = HttpResponse(result.getvalue(), content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="%s.pdf"' %(nombre)
		print(response['Content-Disposition'])
		return response
	return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))