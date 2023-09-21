#***LIBRERÍAS***

import pandas as pd #Manejo de datasets
import numpy as np #Manejo de matrices, vectores y otras operaciones matematicas

#***FUNCIONES***

#funcion que mediante where todo lo que no cumpla con la condición se reemplaza

def where(dataset, columna, condicion, valor, valor_reemplazo, columna_a_remplazar=None):
    # Diccionario que asocia cada tipo de condición con la función correspondiente de pandas
    condiciones = {
        '<': pd.Series.lt,
        '<=': pd.Series.le,
        '>': pd.Series.gt,
        '>=': pd.Series.ge,
        '==': pd.Series.eq,
        '!=': pd.Series.ne
    }
    
    # Obtener la función correspondiente a la condición
    funcion = condiciones[condicion]
    
    # Aplicar la condición a la columna y el valor especificados
    if not columna_a_remplazar:
        resultado = dataset.where(funcion(dataset[columna], valor), valor_reemplazo)
    else:
        dataset[columna_a_remplazar] = dataset[columna_a_remplazar].where(funcion(dataset[columna], valor), valor_reemplazo)
        resultado=dataset
       
    return resultado

def mask(dataset, columna, condicion, valor, valor_reemplazo, columna_a_remplazar=None):
    # Diccionario que asocia cada tipo de condición con la función correspondiente de pandas
    condiciones = {
        '<': pd.Series.lt,
        '<=': pd.Series.le,
        '>': pd.Series.gt,
        '>=': pd.Series.ge,
        '==': pd.Series.eq,
        '!=': pd.Series.ne
    }
    
    # Obtener la función correspondiente a la condición
    funcion = condiciones[condicion]
    
    # Aplicar la condición a la columna y el valor especificados
    if not columna_a_remplazar:
        resultado = dataset.mask(funcion(dataset[columna], valor), valor_reemplazo)
    else:
        dataset[columna_a_remplazar] = dataset[columna_a_remplazar].mask(funcion(dataset[columna], valor), valor_reemplazo)
        resultado=dataset
       
    return resultado

def isinEXC(lim1,lim2,columna=None):
    if not columna:
        resultado=dataset.isin([lim1,lim2])
    else:
        resultado=dataset.isin({columna: [lim1, lim2]})
    return resultado

def isinRANGE(lim1,lim2,columna=None):
    if not columna:
        resultado=dataset.isin(list(range(lim1,lim2)))
    else:
        resultado=dataset.isin({columna: list(range(lim1,lim2))})
    return resultado  


dataset=pd.read_csv('data.csv')
"""
d1=mask(dataset, 'Age', '>=', 50, 0, 'Intensity')
d1=isinEXC(0,2,'Location')
d1=isinRANGE(0,2,'Location')
print(d1)
dataset.where(dataset['Age']>30, 0)
"""