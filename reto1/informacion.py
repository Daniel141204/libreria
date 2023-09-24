#***LIBRERÍAS***

import pandas as pd #Manejo de datasets
import numpy as np #Manejo de matrices, vectores y otras operaciones matematicas
import matplotlib.pyplot as plt #graficación de datos
import seaborn as sns #mapas de calor
import filtrado as f

#***FUNCIONES***

#mapa de calor valor indicado
def mapacalor(dataset, lim1=None, lim2=None, type="RANGE"):
    if not lim1 and not lim2: 
        sns.heatmap(dataset.isnull(), cbar=False)
    elif lim1 and not lim2:
        sns.heatmap(dataset==lim1, cbar=False)
    elif not lim1 and lim2:
        sns.heatmap(dataset==lim2, cbar=False)
    elif lim1 and lim2 and type=="RANGE":
        sns.heatmap(f.isinRANGE(dataset,lim1,lim2), cbar=False)
    else:
        sns.heatmap(f.isinEXC(dataset,lim1,lim2),cbar=False)  
    plt.show() 

#Mapa de calor media
def mapamedia(dataset):
    data_numerica = f.dataType(dataset, ['int64'])
    distancia = data_numerica.sub(data_numerica.mean())
    sns.heatmap(distancia, annot=True,cbar=False)
    sns.set(font_scale=0.8)
    for i, media in enumerate(data_numerica.mean()):
        plt.text(i + 0.5, len(data_numerica) + 0.5, f'{media:.2f}', ha='center', va='top')
    plt.show()

#obtener valor máximo (solamente el valor)
def maxvalue(dataset, columnmax=None, nom_condicion=None, condicion=None):
    if not columnmax:
        resultado=dataset.max()
    else:
        resultado= f.max(dataset, columnmax, nom_condicion, condicion)[columnmax].max()
    return resultado

#obtener valor mínimo (solamente el valor)
def minvalue(dataset, columnmin=None, nom_condicion=None, condicion=None):
    if not columnmin:
        resultado=dataset.min()
    else:
        resultado= f.min(dataset, columnmin, nom_condicion, condicion)[columnmin].min()
    return resultado

#***ESTRUCTURA FUNCIONES***

#mapacalor: dataset, lim1, lim2, type(en rango o exclusivo)       
#mapacalor: dataset
#maxvalue: dataset, columnmax, nom_condicion, condicion
#minvalue: dataset, columnmin, nom_condicion, condicion

d1=pd.read_csv('data.csv')
#mapamedia(d1)

"""
mapacalor(d1)
mapacalor(d1,50)
mapacalor(d1,None,16)
mapacalor(d1,30,42,"EXC")
mapacalor(d1,30,42)
"""