from datetime import datetime
import random
from Factura.models import *
from calendar import monthrange

meses = {
    'ENERO':'01',
    'FEBRERO':'02',
    'MARZO':'03',
    'ABRIL':'04',
    'MAYO':'05',
    'JUNIO':'06',
    'JULIO':'07',
    'AGOSTO':'08',
    'SEPTIEMBRE':'09',
    'OCTUBRE':'10',
    'NOVIEMBRE':'11', 
    'DICIEMBRE':'12',   
}


def obtener_fecha():
    """
    Esta funcion retorna la fecha del dia que se genera la factura (puede no ser conveniente si se quiere generar u factura de meses pasados)
    """
    now = datetime.now()
    dia = str(now.day)
    mes = str(now.month)
    año = str(now.year)

    fecha = dia + "/" + mes + "/" + año

    return str(fecha)


def obtener_fecha2(mes, año):
    """
    Esta función retorna la fecha compuesta por el ultimo dia del mes y año del cual se esta facturando
    """

    nmes = str(meses[mes])
    dia = monthrange(int(año), int(nmes))

    return  f"{str(dia[1])}/{nmes}/{año}"

def obtener_numero_factura(cifcliente, mes, ano):
    """
    Esta funcion de abajo es la que retorna un numero de factura para imprimirla en la factura
    """
    #Este for es un apaño para obtener el numero de la tabla que ocupa en la base de datos
    contador = 0
    #print("El elegido es: " + cifcliente)
    for _cliente in cliente.objects.all():
        #print("Uno de los cif: " + str(_cliente.cif))
        contador = contador +1
        if _cliente.cif == cifcliente:
            break
            
    nmes = str(meses[mes])

    return "F-" + str(nmes) + str(ano) + "/" + str(contador)


def obtener_numero_factura_simple(cifcliente, mes, ano):
    """
    Esta funcion de abajo es la que retorna un numero de factura para imprimirla en la factura simple
    """
    #Este for es un apaño para obtener el numero de la tabla que ocupa en la base de datos
    contador = 0
    #print("El elegido es: " + cifcliente)
    for _cliente in cliente.objects.all():
        #print("Uno de los cif: " + str(_cliente.cif))
        contador = contador +1
        if _cliente.cif == cifcliente:
            break
            
    nmes = str(meses[mes])

    return "FS-" + str(nmes) + str(ano) + "/" + str(contador)



def obtener_datos_temprales():
    """
    Esta funcion de abajo es la que obtiene los datos temporales que estan en la base de datos y se los pasa a la view para que 
    haga las operaciones pertinentes
    """
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


def almacenar_total_factura(array_temporales):
    """
    Esta funcion de abajo es la que calcula el precio final y el precio total de la factura normal
    """
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



def almacenar_total_factura_simple(array_temporales):
    """
    Esta funcion es la que calcula el precio final para la factura simple
    """
    _factura = factura_simple.objects.all().filter(mes=array_temporales[2], año=array_temporales[3], cif_id=array_temporales[1])
    total = 0
    for campo in _factura:
        precio = campo.precio
        total = total + precio
    return float(total)


def almacenar_lavado_sisterna(array):
    """
    Esta funcion tiene en cuenta si esta el lavado de cisterna activada
    """
    try:
        PRECIO_LAVADO_CISTERNA = "80"
        LAVADO = "LAVADO DE CISTERNA"
        SEPARADOR = "**********"
        lavado_repetido = 0
        #Con el _factura y el for compruebo si ya hay un lavado de cisterna en la factura de ese mes y año para no añadirlo duplicado
        _factura = factura.objects.all().filter(mes=array[2], año=array[3], cif_id=array[1])
        for campo in _factura:
            if (campo.origen == LAVADO):
                lavado_repetido = lavado_repetido + 1
                 

        #Esta casuistica es la que hace que se añada un nuevo lavado de sisterna
        if (array[5] == "SI" and lavado_repetido == 0):
            p=factura(cif_id=array[1], nif=SEPARADOR, origen=LAVADO, destino=SEPARADOR, mes=array[2], año=array[3], kg="0", precio=PRECIO_LAVADO_CISTERNA)
            p.save()
        #Esta casuistica elimina lavado de sisterna si ya hay una añadida y la opcion de lavado esta a no
        if(array[5] == "NO" and lavado_repetido == 1):
            factura.objects.filter(cif_id=array[1], nif=SEPARADOR, origen=LAVADO, destino=SEPARADOR, mes=array[2], año=array[3], kg="0", precio=PRECIO_LAVADO_CISTERNA).delete()
    except Exception as e:
        print(repr(e))