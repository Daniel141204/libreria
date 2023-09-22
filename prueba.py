from reto1 import conexion as r
from reto1 import filtrado as f

#                     ***PRUEBA MÓDULO DE CONEXIÓN***

#ORDEN FUNCIÓN: nombre, codigo, index, limite

#Abrir archivo local
print("Dataset local:\n")
d1=r.openCSV("data.csv",None,None,100)
print(d1)

#Abrir archivo remoto
print("Dataset remoto:\n")
d2=r.openCSV('www.datos.gov.co','9ssf-i6c5','cedula', 70)
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
print("Función Where:\n")
d3=f.where(d1.copy(), 'Age', '>=', 50, 'Cambio de valor con where', 'Type')
print(d3)

#Remplazar un valor que cumpla con la condición que se le mande
print("Función Mask:\n")
d4=f.mask(d1.copy(), 'Age', '<=', 30, 'Cambio de valor con mask', 'Type')
print(d4)

#Buscar valores que sean o un número A o un número B
print("Función isinEXC:\n")
d5=f.isinEXC(d1, 30, 50, 'Age')
print(d5)

#Buscar valores que estén entre un número A y un número B
print("Función isinRANGE:\n")
d6=f.isinRANGE(d1, 30, 50, 'Age')
print(d6)

#Busca el máximo de una columna
print("Función en columna:\n")
d7=f.max(d1, 'Age')
print(d7)

#Busca el máximo de una columna con una condición
print("Función en columna + condición:\n")
d8=f.max(d1, 'Age','Intensity', 3)
print(d8)

print(d1)

#d3=filtrado.cumsum(d1,'Age')