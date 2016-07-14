from django.shortcuts import render

import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


def generarPDF(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = io.BytesIO()

    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def myview(request):
	context = {'titulo' : 'Primer PDF generado con Django',
				'contenido' : 'Generado con python 3  reportlab'
	}
	return generarPDF('mytemplate.html', context)