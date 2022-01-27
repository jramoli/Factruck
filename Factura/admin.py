from django.contrib import admin
from Factura.models import *

# Register your models here.
class trasformcliente(admin.ModelAdmin):
    list_display=("cif", "nombre")

class trasformempresa(admin.ModelAdmin):
    list_display=("nif", "nombre", "apellido1", "apellido2")

class trasformfactura(admin.ModelAdmin):
    list_display=("cif", "nif", "origen", "destino", "mes", "año")
    list_filter=("cif", "nif", "origen", "destino", "mes", "año")
    exclude = ('total',)

class trasformfacturasimple(admin.ModelAdmin):
    list_display=("cif", "nif", "mes", "año")
    list_filter=("cif", "nif", "concepto", "mes", "año")

admin.site.register(empresa, trasformempresa)
admin.site.register(cliente, trasformcliente)
admin.site.register(factura, trasformfactura)
admin.site.register(factura_simple, trasformfacturasimple)