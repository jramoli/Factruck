from datetime import datetime
import random
from select import select
import sqlite3

def obtener_fecha():
    now = datetime.now()
    dia = str(now.day)
    mes = str(now.month)
    año = str(now.year)

    fecha = dia + "/" + mes + "/" + año

    return str(fecha)

def obtener_numero_factura():
    numero = str()
    for i in [0,1,2,3,4]:
        numero+= str(random.randint(0, 5))
    return "F-" + numero


