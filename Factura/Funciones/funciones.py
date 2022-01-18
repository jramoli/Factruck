from ast import Return
from datetime import datetime
from http.client import HTTPResponse
import random
from select import select
import sqlite3
from unittest import result
from django.template.loader import get_template


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def obtener_fecha():
    now = datetime.now()
    dia = str(now.day)
    mes = str(now.month)
    año = str(now.year)

    fecha = dia + "/" + mes + "/" + año

    return str(fecha)

def obtener_numero_factura():
    numero = str()
    for i in [0,1,2,3,4]:
        numero+= str(random.randint(0, 5))
    return "F-" + numero

def renderizar_pdf(template_src, contexto):
    template = get_template(template_src)
    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


