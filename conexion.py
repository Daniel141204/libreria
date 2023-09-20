#***LIBRERÍAS***

from sodapy import Socrata #Para obtener datasets de url
import pandas as pd #Manejo de datasets
import numpy as np #Manejo de matrices, vectores y otras operaciones matematicas
import matplotlib.pyplot as plt #graficación de datos
import seaborn as sns #mapas de calor

#***FUNCIONES***

#función que se encarga de recoger el nombre del cvs o la url
"""
def recogerDataset(nombre): 
    
    dataset=abrirCVS(nombre)
    if dataset==False:
       dataset=abrirURL(nombre)
       if dataset==False:
           print("No se encontró ningún archivo con el nombre brindado o con dicha URL")
       else:    
           print("The dataset has been open successfully.")
               

    try:
        dataset=abrirCVS(nombre)
    except Exception as err:
        dataset=abrirURL(nombre)
    return "yo"
    """

#función que se encarga de abrir cvs
def abrirCVS(nombre):
    try:
        dataset=pd.read_csv(nombre)
    except FileNotFoundError:
        dataset=False
    return dataset


#función que se encarga de abrir una url
def abrirCVS(url, codigo):
    try:
        client=Socrata(url, None)
        results=client.get(codigo)
        dataset=pd.DataFrame.from_records(results)
    except FileNotFoundError:
        dataset=False
    return dataset


#función que se encarga de abrir una url con limite
def abrirCVS(url, codigo, limite):
    try:
        client=Socrata(url, None)
        results=client.get(codigo, limit=limite)
        dataset=pd.DataFrame.from_records(results)
    except ConnectionError:
        dataset=False
    return dataset

print("hola soy una prueba\n")
d1=(abrirCVS('www.datos.gov.co','gt2j-8ykr', 50))
d1
print("ya abrí jajaj")

