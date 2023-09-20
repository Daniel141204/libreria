#***LIBRERÍAS***

from sodapy import Socrata #Para obtener datasets de url
import pandas as pd #Manejo de datasets
import numpy as np #Manejo de matrices, vectores y otras operaciones matematicas
import matplotlib.pyplot as plt #graficación de datos
import seaborn as sns #mapas de calor

#***FUNCIONES***

#función que se encarga de recoger el nombre del cvs o la url
def recogerDataset(nombre): 
    try:
        dataset=abrirCVS(nombre)
    return "yo"