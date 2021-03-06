from email.policy import default
from signal import default_int_handler
from django import forms
from Factura.models import *

MES = (
    ('ENERO','ENERO'),
    ('FEBRERO','FEBRERO'),
    ('MARZO','MARZO'),
    ('ABRIL','ABRIL'),
    ('MAYO','MAYO'),
    ('JUNIO','JUNIO'),
    ('JULIO','JULIO'),
    ('AGOSTO','AGOSTO'),
    ('SEPTIEMBRE','SEPTIEMBRE'),
    ('OCTUBRE','OCTUBRE'),
    ('NOVIEMBRE','NOVIEMBRE'),
    ('DICIEMBRE','DICIEMBRE'),
)

CONDICIONAL = (
    ('NO','NO'),
    ('SI','SI'),
)

ANNO = (
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
    ('2025','2025'),
    ('2026','2026'),
    ('2027','2027'),
    ('2028','2028'),
    ('2029','2029'),
    ('2030','2030'),
    ('2031','2031'),
    ('2032','2032'),
    ('2033','2033'),
    ('2034','2034'),
    ('2035','2035'),
    ('2036','2036'),
    ('2037','2037'),
    ('2038','2038'),
    ('2039','2039'),
    ('2040','2040'),
)

class generarfactura(forms.Form):
    empleado = forms.ModelChoiceField(label='Empleado', queryset=empresa.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), required=True)
    cif = forms.ModelChoiceField(label='Cliente', queryset=cliente.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), required=True)
    mes = forms.TypedChoiceField(choices = MES, widget=forms.Select(attrs={'class':'form-select'}), required=True)
    año = forms.TypedChoiceField(choices = ANNO, widget=forms.Select(attrs={'class':'form-select'}), required=True)
    iva = forms.FloatField(required=True, initial=21)
    lavado = forms.ChoiceField(choices = CONDICIONAL, widget=forms.Select(attrs={'class':'form-select'}), required=True)
    retencion = forms.FloatField(required=True, initial=1)


class generarfacturasimple(forms.Form):
    empleado = forms.ModelChoiceField(label='Empleado', queryset=empresa.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), required=True)
    cif = forms.ModelChoiceField(label='Cliente', queryset=cliente.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), required=True)
    mes = forms.TypedChoiceField(choices = MES, widget=forms.Select(attrs={'class':'form-select'}), required=True)
    año = forms.TypedChoiceField(choices = ANNO, widget=forms.Select(attrs={'class':'form-select'}), required=True)
    iva = forms.FloatField(required=True, initial=21)
    retencion = forms.FloatField(required=True, initial=1)
