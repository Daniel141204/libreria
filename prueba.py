from reto1 import conexion as r
from reto1 import filtrado as f

#                     ***PRUEBA MÓDULO DE CONEXIÓN***

#ORDEN FUNCIÓN: nombre, codigo, index, limite

#Abrir archivo local
print("Dataset local:\n")
d1=r.openCSV("data.csv",None,None,170)
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
d8=f.max(d1, 'Age','Intensity', 2)
print(d8)

#Busca el mínimo de una columna
print("Función en columna:\n")
d9=f.min(d1, 'Age')
print(d9)

#Busca el mínimo de una columna con una condición
print("Función en columna + condición:\n")
d10=f.min(d1, 'Age','Intensity', 2)
print(d10)

#Suma los valores de una columna
print("Función en columna:\n")
d11=f.sum(d1, 'Age')
print(d11)

#Suma los valores de una columna con una condición
print("Función en columna + condición:\n")
d12=f.sum(d1, 'Age', 'Intensity', 2)
print(d12)

#Suma acumulada de los valores de una columna
print("Función en columna:\n")
d13=f.cumsum(d1, 'Age')
print(d13)

#Suma acumulada de los valores de una columna con una condición
print("Función en columna + condición:\n")
d14=f.cumsum(d1, 'Age', 'Intensity', 2)
print(d14)

#Generación de un dataset con valores númericos a partir de otro dataset
print("Función DataType:\n")
d15=f.dataType(d1, ['int64'])
print(d15)

#hy
