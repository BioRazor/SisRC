#Para python 3
try:
	import io
#para python 2
except:
	import cStringIO as StringIO

from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

def generarPDF(template_src, context_dict, nombre):
	if not nombre:
		nombre = 'reporte'
	template = get_template(template_src)
	context = context_dict
	html  = template.render(context)
	#para python 3
	try:
		result = io.BytesIO()
		pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
	except:
		result = StringIO.StringIO()
		pdf = pias.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)

	if not pdf.err:
		response = HttpResponse(result.getvalue(), content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="%s.pdf"' %(nombre)
		return response
	return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))