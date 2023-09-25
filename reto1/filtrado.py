## Ana Laura Morcote Chacón 20221020010 y Daniel Felipe Zárate Beltrán 20221020086

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

#funcion que mediante where todo lo que cumpla con la condición se reemplaza

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

#Función que busca valores dentro de unos valores exclusivos

def isinEXC(dataset,lim1,lim2,columna=None):
    if not columna:
        resultado=dataset.isin([lim1,lim2])
    else:
        resultado=dataset.isin({columna: [lim1, lim2]})
    return resultado

#Función que busca valores dentro de un rango

def isinRANGE(dataset,lim1,lim2,columna=None):
    if not columna:
        resultado=dataset.isin(list(range(lim1,lim2)))
    else:
        resultado=dataset.isin({columna: list(range(lim1,lim2))})
    return resultado

def max(dataset, columnmax, nom_condicion=None, condicion=None):
    if not nom_condicion and not condicion:
        resultado=dataset[dataset[columnmax]==dataset[columnmax].max()]
    elif (nom_condicion and not condicion) or (not nom_condicion and condicion):
        resultado=False
    else:
        item = dataset[dataset[nom_condicion]==condicion]
        resultado=item[item[columnmax]==item[columnmax].max()]
    return resultado

def min(dataset, columnmin, nom_condicion=None, condicion=None):
    if not nom_condicion and not condicion:
        resultado=dataset[dataset[columnmin]==dataset[columnmin].min()]
    elif (nom_condicion and not condicion) or (not nom_condicion and condicion):
        resultado=False
    else:
        item = dataset[dataset[nom_condicion]==condicion]
        resultado=item[item[columnmin]==item[columnmin].min()]
    return resultado

def sum(dataset, columnsum, nom_condicion=None, condicion=None):
    if not nom_condicion and not condicion:
        resultado=dataset[columnsum].sum()
    elif (nom_condicion and not condicion) or (not nom_condicion and condicion):
        resultado=False
    else:
        resultado=dataset[columnsum][dataset[nom_condicion] == condicion].sum()

    return resultado

def cumsum(dataset, columnsum, nom_condicion=None, condicion=None):
    if not nom_condicion and not condicion:
        resultado=dataset[columnsum].cumsum()
    elif (nom_condicion and not condicion) or (not nom_condicion and condicion):
        resultado=False
    else:
        resultado=dataset[columnsum][dataset[nom_condicion] == condicion].cumsum()

    return resultado

def dataType(dataset, types):
    data = dataset.select_dtypes(include=types)
    return data

def groupncount(dataset, categorias):
    return dataset.groupby(categorias)[categorias[1]].count()

def groupncount_equal(dataset, categoria, nom_condicion, valor, index):
    return dataset[dataset[nom_condicion]==valor].groupby(categoria)[index].count()

def groupncount_differ(dataset, categoria, nom_condicion, valor, index):
    return dataset[dataset[nom_condicion]!=valor].groupby(categoria)[index].count()


#***ESTRUCTURA FUNCIONES***

#where: dataset, columna, condicion, valor, valor_reemplazo, columna_a_remplazar
#mask: dataset, columna, condicion, valor, valor_reemplazo, columna_a_remplazar
#isinEXC: dataset, lim1, lim2, columna
#isinRANGE: dataset, lim1, lim2, columna
#max: dataset, columnmax, nom_condicion, condicion
#min: dataset, columnmin, nom_condicion, condicion
#sum: dataset, columnsum, nom_condicion, condicion
#cumsum: dataset, columnsum, nom_condicion, condicion
#dataType: dataset, tipos de dato (como lista). Ej:['float64', 'int64', 'bool', 'string', 'char', 'object', 'number' ])
#groupncount: dataset, categorias (como lista). Ej:['Age', 'Type']
#groupncount_equal: dataset, categoria, nom_condicion, valor, index
#groupncount_differ: dataset, categoria, nom_condicion, valor, index



"""
data=pd.read_csv('data.csv')
d1=where(data, 'Age', '>=', 50, 0, 'Intensity')
print(d1)

d1=isinEXC(0,2,'Location')
d1=isinRANGE(0,2,'Location')

"""