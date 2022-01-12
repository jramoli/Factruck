import json
import os
import pdfkit
class method:

    def __init__(self):
        self.url = None    # creates a new empty list for each dog

    def read_json(self, elemento):
        """
        Este metodo obtiene un nombre de elemento y la busca en el archivo conf.json
        @param nombre clave del elemento que quieres buscar en el json
        """
        with open(os.getcwd() + "/Factruck/conf/conf.json") as json_file:
            json_file = json.load(json_file)    #Aqui combertimos los objetos a json que entiende python
            for dato in json_file:
                self.url = dato.get(elemento)
        return self.url
    
    def crear_pdf(html):
        """
        Crea un pdf que se almacena en el escritorio de la aplicación y lo sirve en una respuestahttp
        @param: recoge un html que transforma en pdf
        """
        options = {'enable-local-file-access': None}    #Esta linea es para que nos permita acceso a las imagenes del pdf (por seguridad vienen deshabilitado)
        path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_string(html, "Facturacion.pdf", options=options, configuration=config)