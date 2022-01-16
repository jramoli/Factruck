from django.contrib import admin
from Factura.models import *

# Register your models here.
class trasformcliente(admin.ModelAdmin):
    list_display=("cif", "nombre")

class trasformempresa(admin.ModelAdmin):
    list_display=("nif", "nombre", "apellido1", "apellido2")

class trasformfactura(admin.ModelAdmin):
    list_display=("cif", "origen", "destino", "mes", "año")
    list_filter=("cif", "origen", "destino", "mes", "año")

class trasformfacturasimple(admin.ModelAdmin):
    list_display=("nif", "mes", "año")
    list_filter=("nif", "concepto", "mes", "año")

admin.site.register(empresa, trasformempresa)
admin.site.register(cliente, trasformcliente)
admin.site.register(factura, trasformfactura)
admin.site.register(factura_simple, trasformfacturasimple)