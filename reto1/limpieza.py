#LIBRERÍAS

from sodapy import Socrata #Para obtener datasets de url
import pandas as pd #Manejo de datasets
import numpy as np #Manejo de matrices, vectores y otras operaciones matematicas
import matplotlib.pyplot as plt #graficación de datos
import seaborn as sns #mapas de calor

#FUNCIONES

#Funcion que nos deja eliminar las filas que tengan algun nan
def dropNanALGUN(dataset):
    #dataset.dropna(axis=0, how='any', inplace=False)
    return dataset.dropna(axis=0, how='any',  inplace=False)

#Funcion que nos deja eliminar las filas que tengan todos los valores nan
def dropNanTODOS(dataset):
    #dataset.dropna(axis=0, how='all', inplace=False)
    return dataset.dropna(axis=0, how='all',  inplace=False)

#Funcion que nos deja eliminar las columnas que tengan algun nan
def dropNanALGUNCOL(dataset):
    #dataset.dropna(axis=1, how='any', inplace=False)
    return dataset.dropna(axis=1, how='any',  inplace=False)

#Funcion que nos deja eliminar las columnas que tengan todos los valores nan
def dropNanTODOSCOL(dataset):
    #dataset.dropna(axis=1, how='all', inplace=False)
    return dataset.dropna(axis=1, how='all',  inplace=False)

#Funcion que rellena los NaN con un valor fijo
def fillNan(dataset, valor):
    return dataset.fillna(valor)

#Funcion que rellena los NaN con el promedio de cada columna que sea numerica, si hay columnas que no son numericas, las deja igual

def fillna_numericas(dataset):
    
    columnas_numericas = dataset.select_dtypes(include='number').columns
    for column in columnas_numericas:
        mean = dataset[column].mean()
        dataset[column].fillna(mean, inplace=True)
    return dataset

#Funcion que rellena los NaN con el valor de adelante proyectando el valor hacia atrás hasta un limite definido por el usuario)
def fillNanBack(dataset, limite):
    return dataset.fillna(method='bfill', limit=limite)

#Funcion que rellena los NaN con el valor de adelante proyectando el valor hacia adelante hasta un limite definido por el usuario)
def fillNanFront(dataset, limite):
    return dataset.fillna(method='ffill', limit=limite)

#Función que borre en todo el dataset un valor fijo que el usuario defina
def dropValue(dataset, valor):
    return dataset.replace(valor, np.nan).dropna(axis=0, how='any', inplace=False)

#Función que borre el valor deseado en una columna especifica

import numpy as np
import pandas as pd

def dropValueColumna(dataset, valor, columna):
    dataset[columna].replace(valor, np.nan, inplace=True)
    dataset.dropna(subset=[columna], inplace=True)
    return dataset


data=pd.read_csv('data.csv')
for i in range(100):
  data.iloc[[np.random.randint(1, 400)],[0]] = np.nan
  data.iloc[[np.random.randint(1, 400)],[1]] = np.nan
  data.iloc[[np.random.randint(1, 400)],[2]] = np.nan
  data.iloc[[np.random.randint(1, 400)],[3]] = np.nan
d4=dropNanALGUN(data)
print(d4)

d5=dropNanTODOS(data)
print(d5)

d6=dropNanALGUNCOL(data)
print(d6)

d7=dropNanTODOSCOL(data)
print(d7)

d8=fillNan(data, 0)
print(d8)

d9=fillna_numericas(data)
print(d9)

d10=fillNanBack(data, 2)
print(d10)

d11=fillNanFront(data, 2)
print(d11)

d12=dropValue(data, 3)
print(d12)

d13=dropValueColumna(data, 3, 'Intensity')
print(d13)

#hy