from array import array
from urllib import response
import django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.shortcuts import render
from Factura.Funciones.funciones import *
from Factura.formulario.formularios import *
import os
import pdfkit

BASE_DIR = os.path.dirname(os.path.realpath(__file__))



def view_html_factura(request):
    #Esta funcion devuelve un array con los datos del formulario
    array_temporales = obtener_datos_temprales()
    almacenar_lavado_sisterna(array_temporales)
    #En estas lineas de abajo obtengo los datos de cliente y empresas segun los datos del formulario
    _cliente = cliente.objects.all().filter(cif=array_temporales[1])
    _empresa = empresa.objects.all().filter(id=array_temporales[0])
    #En esta funcion se calcula el precio y devuelve un total de todos las lineas
    total = almacenar_total_factura(array_temporales)
    iva = total * (float(array_temporales[4]) / 100)
    retencion = total * (float(array_temporales[6]) / 100)
    precio_final = total + iva - retencion
    _factura_con_precio = factura.objects.all().filter(
        cif_id=array_temporales[1], mes=array_temporales[2], año=array_temporales[3])
    nfactura = obtener_numero_factura(array_temporales[0], array_temporales[2], array_temporales[3])
    contexto = {
        'facturas': _factura_con_precio,
        'clientes': _cliente,
        'empresas': _empresa,
        'fecha': obtener_fecha,
        'numero_factura': nfactura,
        'mes': array_temporales[2],
        'año': array_temporales[3],
        'cantidad_iva': array_temporales[4],
        'cantidad_retencion': array_temporales[6],
        'total': round(total,2),
        'iva': round(iva,2),
        'retencion': round(retencion,2),
        'precio_total': round(precio_final,2),
    }
    print(contexto['facturas'])
    return render(request, "factura.html", contexto)


def view_html_factura_simple(request):
    array_temporales = obtener_datos_temprales()
    _cliente = cliente.objects.all().filter(cif=array_temporales[1])
    _empresa = empresa.objects.all().filter(id=array_temporales[0])
    total = almacenar_total_factura_simple(array_temporales)
    iva = total * (float(array_temporales[4]) / 100)
    retencion = total * (float(array_temporales[6]) / 100)
    precio_total = total + iva - retencion
    _factura_con_precio = factura_simple.objects.all().filter(
        cif_id=array_temporales[1], mes=array_temporales[2], año=array_temporales[3])
    contexto = {
        'facturas': _factura_con_precio,
        'clientes': _cliente,
        'empresas': _empresa,
        'fecha': obtener_fecha,
        'numero_factura': obtener_numero_factura,
        'mes': array_temporales[2],
        'año': array_temporales[3],
        'cantidad_iva': array_temporales[4],
        'cantidad_retencion': array_temporales[6],
        'total': round(total,2),
        'iva': round(iva,2), 
        'retencion': round(retencion,2),
        'precio_total': round(precio_total,2),
    }
    return render(request, "factura_simple.html", contexto)

@login_required
def view_pdf_factura(request):
    if request.method == 'POST':
        """ ------------------------------------obtengo los datos del form------------------------------------"""
        _empleado = request.POST.get('empleado')
        _cif = request.POST.get('cif')
        _mes = request.POST.get('mes')
        _año = request.POST.get('año')
        _iva = request.POST.get('iva')
        _lavado = request.POST.get('lavado')
        _retencion = request.POST.get('retencion')

        temporal.objects.filter(id=1).update(empleado=_empleado)
        temporal.objects.filter(id=1).update(cif=_cif)
        temporal.objects.filter(id=1).update(mes=_mes)
        temporal.objects.filter(id=1).update(año=_año)
        temporal.objects.filter(id=1).update(iva=_iva)
        temporal.objects.filter(id=1).update(lavado=_lavado)
        temporal.objects.filter(id=1).update(retencion=_retencion)
        temporal.objects.filter(id=1).update(kilosminimos="25000")

        #path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdf = pdfkit.from_url('http://127.0.0.1:5000/factura/', configuration=config)
        response = HttpResponse(pdf, content_type='application/pdf')

        return response
    else:
        form1 = generarfactura()
        return render(request, 'formfactura.html', {'form1': form1})

@login_required
def view_pdf_factura_simple(request):
    if request.method == 'POST':
        """ ------------------------------------obtengo los datos del form------------------------------------"""
        _empleado = request.POST.get('empleado')
        _cif = request.POST.get('cif')
        _mes = request.POST.get('mes')
        _año = request.POST.get('año')
        _iva = request.POST.get('iva')
        _retencion = request.POST.get('retencion')

        temporal.objects.filter(id=1).update(empleado=_empleado)
        temporal.objects.filter(id=1).update(cif=_cif)
        temporal.objects.filter(id=1).update(mes=_mes)
        temporal.objects.filter(id=1).update(año=_año)
        temporal.objects.filter(id=1).update(iva=_iva)
        temporal.objects.filter(id=1).update(retencion=_retencion)

        #path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdf = pdfkit.from_url('http://127.0.0.1:5000/factura_simple/', configuration=config)
        response = HttpResponse(pdf, content_type='application/pdf')
        return response
    else:
        form2 = generarfacturasimple()
        return render(request, 'formfacturasimple.html', {'form2': form2})