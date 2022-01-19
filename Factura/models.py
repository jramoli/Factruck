from django.db import models
from django.db.models.fields.related import ForeignKey
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

class temporal(models.Model):
    empleado=models.CharField(max_length=50)
    cif=models.CharField(max_length=50)
    mes=models.CharField(max_length=50)
    año=models.CharField(max_length=50)
    iva=models.CharField(max_length=50)
    lavado=models.CharField(max_length=50)
    retencion=models.CharField(max_length=50)
    kilosminimos=models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.nombre)

class empresa(models.Model):
    nif=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    apellido1=models.CharField(max_length=50)
    apellido2=models.CharField(max_length=50)
    calle=models.CharField(max_length=50)
    movil=models.CharField(max_length=50)
    cp=models.CharField(max_length=50, default='41520')
    localidad=models.CharField(max_length=50, default='EL VISO DEL ALCOR')
    provincia=models.CharField(max_length=50, default='Sevilla')
    matricula=models.CharField(max_length=50)
    matricula_remolque=models.CharField(max_length=50)
    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido1, self.apellido2)

class cliente(models.Model):
    cif=models.CharField(max_length=50, primary_key = True)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    provincia=models.CharField(max_length=50)
    poblacion=models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.nombre)

class factura(models.Model):
    cif=ForeignKey(cliente, on_delete=models.CASCADE)
    nif=models.CharField(max_length=50)
    origen=models.CharField(max_length=50)
    destino=models.CharField(max_length=50)
    mes=models.CharField(max_length=50, choices=MES)
    año=models.CharField(max_length=50, choices=ANNO)
    kg=models.FloatField(default=0.0)
    precio=models.FloatField(default=0.0)
    total=models.FloatField(default=0.0)
    def __str__(self):
        return '%s %s %s %s %s' % (self.cif, self.origen, self.destino, self.mes, self.año)

class factura_simple(models.Model):
    cif=ForeignKey(cliente, on_delete=models.CASCADE)
    nif=models.CharField(max_length=50)
    concepto=models.TextField(max_length=1000)
    mes=models.CharField(max_length=50, choices=MES)
    año=models.CharField(max_length=50, choices=ANNO)
    precio=models.FloatField(default=0.0)
    def __str__(self):
        return '%s %s' % (self.cif, self.concepto)
