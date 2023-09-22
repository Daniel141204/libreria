#***LIBRERÍAS***

from sodapy import Socrata #Para obtener datasets de url
import pandas as pd #Manejo de datasets

#***FUNCIONES***

#función que se encarga de recoger el nombre del cvs o la url, con el código y limite

def openCSV(nombre=None, codigo=None, Index=None, limite=None): #Parametros nombre(nombre del archivo ó URL), en caso de ser url, pide el id, y puede pedir también el límite
    
    #ABRIR ARCHIVO LOCAL
    if nombre and not codigo and not Index and not limite: #Cuando solo hay 'nombre', asume que es un archivo.csv y utiliza el método de pandas
        try:
            dataset=pd.read_csv(nombre)
        except FileNotFoundError: #Si no encuentra un archivo, retorna false
            dataset=False
        return dataset
    elif nombre and not codigo and Index and not limite:
        try:
            dataset=pd.read_csv(nombre, index_col=Index)
        except FileNotFoundError: #Si no encuentra un archivo, retorna false
            dataset=False
        return dataset
    elif nombre and not codigo and Index and limite:
        try:
            dataset=pd.read_csv(nombre, index_col=Index, nrows=limite)
        except FileNotFoundError: #Si no encuentra un archivo, retorna false
            dataset=False
        return dataset
    elif nombre and not codigo and not Index and limite:
        try:
            dataset=pd.read_csv(nombre, nrows=limite)
        except FileNotFoundError: #Si no encuentra un archivo, retorna false
            dataset=False
        return dataset  

    #ABRIR ARCHIVO REMOTO     
    elif nombre and codigo and not Index and not limite: #Cuando hay 'nombre' y 'código', asume que es un dataset remoto y utiliza el método de Socrata, mas obtiene el dataset completo
        try:
            client=Socrata(nombre, None)
            results=client.get(codigo)
            dataset=pd.DataFrame.from_records(results)
        except ConnectionError: #Si hay un error de conexión, retorna false
            dataset=False
        return dataset
    elif nombre and codigo and not Index and limite: #Cuando hay 'nombre' y 'código', asume que es un dataset remoto y utiliza el método de Socrata limitando el dataset a lo indicado en 'limite'
        try:
            client=Socrata(nombre, None)
            results=client.get(codigo, limit=limite)
            dataset=pd.DataFrame.from_records(results)
        except ConnectionError: #Si hay un error de conexión, retorna false
            dataset=False
        return dataset
    elif nombre and codigo and Index and not limite: #Cuando hay 'nombre' y 'código', asume que es un dataset remoto y utiliza el método de Socrata limitando el dataset a lo indicado en 'limite'
        try:
            client=Socrata(nombre, None)
            results=client.get(codigo)
            dataset=pd.DataFrame.from_records(results)
            dataset=dataset.set_index(Index)
        except ConnectionError: #Si hay un error de conexión, retorna false
            dataset=False
        return dataset        
    elif nombre and codigo and Index and limite:
        try:
            client=Socrata(nombre, None)
            results=client.get(codigo, limit=limite)
            dataset=pd.DataFrame.from_records(results)
            dataset=dataset.set_index(Index)
        except ConnectionError: #Si hay un error de conexión, retorna false
            dataset=False
        return dataset 

    else:
        return False #Si ninguna de las condiciones se cumple retorna false


#ORDEN FUNCIÓN: nombre, codigo, index, limite

#d1=openCSV('www.datos.gov.co','9ssf-i6c5','cedula', 20)
#d1=openCSV('Base_de_datos_beneficiarios_Colombia_mayor..csv', None, 'cedula', 20)
#print(d1)


