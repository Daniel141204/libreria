#***LIBRERÍAS***

import pandas as pd #Manejo de datasets
import numpy as np #Manejo de matrices, vectores y otras operaciones matematicas

#***FUNCIONES***

#funcion que mediante where todo lo que no cumpla con la condición se reemplaza

def where(dataset, columna, condicion, valor, valor_reemplazo):
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
    resultado = dataset.where(funcion(dataset[columna], valor), valor_reemplazo)
    
    
    return resultado

dataset=pd.read_csv('data.csv')
d1=where(dataset, 'Age', '>=', 50, 0)
print(d1)
#dataset.where(dataset['Age']>30, 0)