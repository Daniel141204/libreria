from reto1 import conexion as r
from reto1 import filtrado as f

#                     ***PRUEBA MÓDULO DE CONEXIÓN***

#ORDEN FUNCIÓN: nombre, codigo, index, limite

#Abrir archivo local
d1=r.openCSV("data.csv")
print(d1)

#Abrir archivo remoto
d2=r.openCSV('www.datos.gov.co','9ssf-i6c5',None, 70)
print(d2)


#                     ***PRUEBA MÓDULO DE FILTRADO***

#***ESTRUCTURA FUNCIONES***

    #where: dataset, columna, condicion, valor, valor_reemplazo, columna_a_remplazar
    #mask: dataset, columna, condicion, valor, valor_reemplazo, columna_a_remplazar
    #isinEXC: dataset, lim1, lim2, columna
    #isinRANGE: dataset, lim1, lim2, columna
    #max: dataset, columnmax, nom_condicion, condicion
    #min: dataset, columnmin, nom_condicion, condicion
    #sum: dataset, columnsum, nom_condicion, condicion
    #cumsum: dataset, columnsum, nom_condicion, condicion


#Remplazar un valor que no cumpla con la condición que se le mande
d3=f.where(d1, 'Age', '>=', 50, 'Cambio de valor', 'Type')
print(d3)

#d3=filtrado.cumsum(d1,'Age')