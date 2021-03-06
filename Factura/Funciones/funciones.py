from datetime import datetime
import random
from Factura.models import *
"""
ESta funcion de abajo es la que se encarga de extraer la fecha de hoy para imprimirla en el pdf
"""
def obtener_fecha():
    now = datetime.now()
    dia = str(now.day)
    mes = str(now.month)
    año = str(now.year)

    fecha = dia + "/" + mes + "/" + año

    return str(fecha)

"""
Esta funcion de abajo es la que retorna un numero de factura para imprimirla en la factura
"""
def obtener_numero_factura():
    numero = str()
    for i in [0,1,2,3,4]:
        numero+= str(random.randint(0, 5))
    return "F-" + numero


"""
Esta funcion de abajo es la que obtiene los datos temporales que estan en la base de datos y se los pasa a la view para que 
haga las operaciones pertinentes
"""
def obtener_datos_temprales():
    array_temporales = []
    _temporal = temporal.objects.all()
    for campo in _temporal:
        array_temporales.append(campo.empleado)
        array_temporales.append(campo.cif)
        array_temporales.append(campo.mes)
        array_temporales.append(campo.año)
        array_temporales.append(campo.iva)
        array_temporales.append(campo.lavado)
        array_temporales.append(campo.retencion)
        array_temporales.append(campo.kilosminimos)

    if not array_temporales:
        array_temporales = None
        return array_temporales
    else:
        return array_temporales

"""
Esta funcion de abajo es la que calcula el precio final y el precio total de la factura normal
"""
def almacenar_total_factura(array_temporales):
    _factura = factura.objects.all().filter(mes=array_temporales[2], año=array_temporales[3], cif_id=array_temporales[1])
    total = 0
    for campo in _factura:
        _id = campo.id
        kg = campo.kg
        precio = campo.precio
        if (campo.origen == "LAVADO DE CISTERNA"):
            factura.objects.filter(id=_id).update(total=precio)
            total = total + (precio)
        else:
            factura.objects.filter(id=_id).update(total=round(precio * (kg / 1000), 2))
            total = total + (precio * (kg / 1000))
    return float(total)


"""
Esta funcion es la que calcula el precio final para la factura simple
"""
def almacenar_total_factura_simple(array_temporales):
    _factura = factura_simple.objects.all().filter(mes=array_temporales[2], año=array_temporales[3], cif_id=array_temporales[1])
    total = 0
    for campo in _factura:
        precio = campo.precio
        total = total + precio
    return float(total)

"""
Esta funcion tiene en cuenta si esta el lavado de cisterna activada
"""
def almacenar_lavado_sisterna(array):
    try:
        lavado_repetido = 0
        #Con el _factura y el for compruebo si ya hay un lavado de cisterna en la factura de ese mes y año para no añadirlo duplicado
        _factura = factura.objects.all().filter(mes=array[2], año=array[3], cif_id=array[1])
        for campo in _factura:
            if (campo.origen == "LAVADO DE CISTERNA"):
                lavado_repetido = lavado_repetido + 1
                 
        LAVADO = "LAVADO DE CISTERNA"
        SEPARADOR = "**********"
        if (array[5] == "SI" and lavado_repetido == 0):
            p=factura(cif_id=array[1], nif=SEPARADOR, origen=LAVADO, destino=SEPARADOR, mes=array[2], año=array[3], kg="0", precio="80")
            p.save()
        if(array[5] == "NO" and lavado_repetido == 1):
            factura.objects.filter(cif_id=array[1], nif=SEPARADOR, origen=LAVADO, destino=SEPARADOR, mes=array[2], año=array[3], kg="0", precio="80").delete()
    except Exception as e:
        print(repr(e))