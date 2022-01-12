import django
from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from Factura.formulario.formularios import generarfactura, generarfacturasimple
# Create your views here.

@login_required
def view_generar_factura(request):
    if request.method == 'POST':
        """Por ahora nada"""
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