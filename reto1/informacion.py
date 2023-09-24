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
        sns.heatmap(f.isinRANGE(dataset,lim1,lim2), annot=True,cbar=False)
    else:
        sns.heatmap(f.isinEXC(dataset,lim1,lim2), cbar=False)  
    plt.show()    


d1=pd.read_csv('data.csv')
mapacalor(d1,30,42)
"""
mapacalor(d1)
mapacalor(d1,50)
mapacalor(d1,None,16)
mapacalor(d1,30,42,"EXC")

"""