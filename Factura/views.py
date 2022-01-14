import django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Factura.formulario.formularios import generarfactura, generarfacturasimple
from Factura.models import *
# Create your views here.

@login_required
def view_generar_factura(request):
    if request.method == 'POST':
        _cif = request.POST.get('cif')
        _mes = request.POST.get('mes')
        _año = request.POST.get('año')
        _iva = request.POST.get('iva')
        _lavado = request.POST.get('lavado')
        _retencion = request.POST.get('retencion')
        _kilosminimos = request.POST.get('kilosminimos')
        _factura = factura.objects.filter(cif=_cif, mes=_mes, año=_año)
        return render (request, "lista.html", {"lista" : _factura})
    else:
        form1 = generarfactura()
        return render(request,'formfactura.html',{'form1':form1})

@login_required
def view_generar_factura_simple(request):
    if request.method == 'POST':
        """Por ahora nada"""
    else:
        form2 = generarfacturasimple()
        return render(request,'formfacturasimple.html',{'form2':form2})