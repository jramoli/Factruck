import django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.shortcuts import render
from Factura.Funciones.funciones import *
from Factura.formulario.formularios import *
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

@login_required
def view_generar_factura(request):
    if request.method == 'POST':
        """ ------------------------------------Calcular factura------------------------------------"""
        _empleado = request.POST.get('empleado')
        _cif = request.POST.get('cif')
        _mes = request.POST.get('mes')
        _año = request.POST.get('año')
        _iva = request.POST.get('iva')
        _lavado = request.POST.get('lavado')
        _retencion = request.POST.get('retencion')
        _kilosminimos = request.POST.get('kilosminimos')
        _factura = factura.objects.all().filter(cif=_cif, mes=_mes, año=_año)
        _cliente = cliente.objects.all().filter(cif=_cif)
        _empresa = empresa.objects.all().filter(id=_empleado)
        total = 0
        for campo in _factura:
            _id = campo.id
            kg =  campo.kg
            precio = campo.precio
            factura.objects.filter(id=_id).update(total=precio * kg)
            total = total + (precio * kg)
        iva = total * (float(_iva) / 100)
        retencion = total * (float(_retencion) / 100)
        precio_total = total + iva + retencion
        _factura_con_precio = factura.objects.all().filter(cif=_cif, mes=_mes, año=_año)
        contexto = {
            'facturas' : _factura_con_precio,
            'clientes' : _cliente,
            'empresas' : _empresa,
            'fecha' : obtener_fecha,
            'numero_factura' : obtener_numero_factura,
            'mes' : _mes,
            'año' : _año,
            'cantidad_iva' : _iva,
            'cantidad_retencion' : _retencion,
            'total': round(total,2),
            'iva' : round(iva,2),
            'retencion' : round(retencion, 2),
            'precio_total' : round(precio_total, 2)
        }
        pdf = renderizar_pdf( BASE_DIR + '/../Factura/template/factura.html', contexto)
        return HttpResponse(pdf, content_type='application/pdf')
        #return render (request, "factura.html" ,contexto)
    else:
        form1 = generarfactura()
        return render(request,'formfactura.html',{'form1':form1})

@login_required
def view_generar_factura_simple(request):
    if request.method == 'POST':
        """ ------------------------------------Calcular factura simple------------------------------------"""
        _empleado = request.POST.get('empleado')
        _cif = request.POST.get('cif')
        _mes = request.POST.get('mes')
        _año = request.POST.get('año')
        _iva = request.POST.get('iva')
        _retencion = request.POST.get('retencion')
        _factura = factura_simple.objects.all().filter(cif=_cif, mes=_mes, año=_año)
        _cliente = cliente.objects.all().filter(cif=_cif)
        _empresa = empresa.objects.all().filter(id=_empleado)
        total = 0
        for campo in _factura:
            precio = campo.precio
            total = total + precio
        iva = total * (float(_iva) / 100)
        retencion = total * (float(_retencion) / 100)
        precio_total = total + iva + retencion
        _factura_con_precio = factura_simple.objects.all().filter(cif=_cif, mes=_mes, año=_año)
        contexto = {
            'facturas' : _factura_con_precio,
            'clientes' : _cliente,
            'empresas' : _empresa,
            'fecha' : obtener_fecha,
            'numero_factura' : obtener_numero_factura,
            'mes' : _mes,
            'año' : _año,
            'cantidad_iva' : _iva,
            'cantidad_retencion' : _retencion,
            'total': round(total,2),
            'iva' : round(iva,2),
            'retencion' : round(retencion, 2),
            'precio_total' : round(precio_total, 2)
        }
        return render (request, "factura_simple.html" ,contexto)
    else:
        form2 = generarfacturasimple()
        return render(request,'formfacturasimple.html',{'form2':form2})