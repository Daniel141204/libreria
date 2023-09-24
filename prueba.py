from reto1 import conexion as r
from reto1 import filtrado as f
from reto1 import limpieza as l
from reto1 import informacion as i



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
    #dataType: dataset, tipos de dato (como lista). Ej:['float64', 'int64', 'bool', 'string', 'char', 'object', 'number' ])
    #groupncount: dataset, categorias (como lista). Ej:['Age', 'Type']
    #groupncount_equal: dataset, categoria, nom_condicion, valor, index
    #groupncount_differ: dataset, categoria, nom_condicion, valor, index


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

#                     ***PRUEBA MÓDULO DE LIMPIEZA***

#***ESTRUCTURA FUNCIONES***

    #nanAleatorio: dataset, probabilidad
    #nanAleatorioColumna: dataset, probabilidad, columna
    #nanAleatorioFila: dataset, probabilidad, filas
    #dropNanALGUN: dataset
    #dropNanTODOS: dataset
    #dropNanALGUNCOL: dataset
    #dropNanTODOSCOL: dataset
    #fillNan: dataset, valor
    #fillna_numericas: dataset
    #fillNanBack: dataset, limite
    #fillNanFront: dataset, limite
    #dropValue: dataset, valor
    #dropValueColumna: dataset, valor, columna

#Generación de valores NaN aleatorios en todo el dataset
print("Función nanAleatorio:\n")
d19=l.nanAleatorio(d1, 0.5)
print(d19)

#Generación de valores NaN aleatorios en una columna
print("Función nanAleatorioColumna:\n")
d20=l.nanAleatorioColumna(d1, 0.5, "Duration")
print(d20)

#Generación de valores NaN aleatorios en una fila
print("Función nanAleatorioFila:\n")
d21=l.nanAleatorioFila(d1, 0.7, [0, 1, 2])
print(d21)

#Borrar filas con algún valor NaN
print("Función dropNanALGUN:\n")
d22=l.dropNanALGUN(d1)
print(d22)

#Borrar filas con todos los valores NaN
print("Función dropNanTODOS:\n")
d23=l.dropNanTODOS(d1)
print(d23)

#Borrar columnas con algún valor NaN
print("Función dropNanALGUNCOL:\n")
d24=l.dropNanALGUNCOL(d1)
print(d24)

#Borrar columnas con todos los valores NaN
print("Función dropNanTODOSCOL:\n")
d25=l.dropNanTODOSCOL(d1)
print(d25)

#Rellenar los valores NaN con un valor fijo
print("Función fillNan:\n")
d26=l.fillNan(d1, 435)
print(d26)

#Rellenar los valores NaN con el valor de la media
print("Función fillna_numericas:\n")
d27=l.fillna_numericas(d1)
print(d27)

#Rellenar los valores NaN con el valor de atrás proyectando el valor hacia atrás hasta un limite definido por el usuario
print("Función fillNanBack:\n")
d28=l.fillNanBack(d1, 2)
print(d28)

#Rellenar los valores NaN con el valor de adelante proyectando el valor hacia adelante hasta un limite definido por el usuario
print("Función fillNanFront:\n")
d29=l.fillNanFront(d1, 2)
print(d29)

#Borrar en todo el dataset un valor fijo que el usuario defina
print("Función dropValue:\n")
d30=l.dropValue(d1, 3)
print(d30)

#Borrar el valor deseado en una columna especifica
print("Función dropValueColumna:\n")
d31=l.dropValueColumna(d1, 3, 'Intensity')
print(d31)

#                     ***PRUEBA MÓDULO DE INFORMACIÓN***

#***ESTRUCTURA FUNCIONES***

    #mapacalor: dataset, lim1, lim2, type(en rango o exclusivo)
    #mapacalor: dataset
    #maxvalue: dataset, columnmax, nom_condicion, condicion
    #minvalue: dataset, columnmin, nom_condicion, condicion
    #contar: dataset, valor, columna

#Mapa de calor con valores NaN
print("Función mapacalor:\n")
d32=i.mapacalor(d1, 50, 70, "EXC")
print(d32)

#Mapa de calor sin valores NaN
print("Función mapacalor:\n")
d33=i.mapacalor(d19)
print(d33)

#Mapa de calor valor media
print("Función mapamedia:\n")
d34=i.mapamedia(d1)
print(d34)

#Obtener valor máximo (solamente el valor)
print("Función maxvalue:\n")
d35=i.maxvalue(d1, 'Age')
print(d35)

#Obtener valor máximo (solamente el valor) con una condición
print("Función maxvalue + condición:\n")
d36=i.maxvalue(d1, 'Age', 'Intensity', 1)
print(d36)

#Obtener valor mínimo (solamente el valor)
print("Función minvalue:\n")
d37=i.minvalue(d1, 'Age')
print(d37)

#Obtener valor mínimo (solamente el valor) con una condición
print("Función minvalue + condición:\n")
d38=i.minvalue(d1, 'Age', 'Intensity', 1)
print(d38)

#Contar valores
print("Función contar:\n")
d39=i.contar(d1, 2)
print(d39)

#Contar valores en una columna
print("Función contar:\n")
d40=i.contar(d1, 30, 'Age')
print(d40)

d41=i.valoresConsecutivos(d19,'Age')
print (d41)