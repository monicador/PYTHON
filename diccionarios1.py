'''
Un Diccionario en Python es un conjunto no ordenado de
pares clave:valor.

Los Diccionarios se encuentran en otros lenguajes como
arreglos asociativo.

El Diccionario en Python es una estructura de datos, tipo de dato 
que nos permite almacenar valores, como enteros, cadenas y funciones,
entreo otros.

Los Diccionarios son contenedores, donde cada elemento
(item) que contiene representa la estructura llave:valor

Cada elemento del diccionario lo identificamos con una clave (key).

Los Diccionarios se indexan con claves, cadenas y numeros
pueden ser claves.

Con un par de llaves se crea un diccionario.

Una lista de pares clave:valor se añade al diccionario
separados por coma (,) entre las llaves

'''


# Crear un Diccionario
movil = {"Jorge" : 3120005412, "Martha": 3001234587}
print(movil)

# Añadir una Clave y su valor al diccionario
movil["Pedro"] = 3136214512
print(movil)


'''
El metodo dict() de los Diccionarios recibe como parametro una
representacion de un diccionario y devuelve un diccionaro de datos.
'''

# La sentencia (del) en el Diccionario elemina una Clave y su valor

movil = dict(Jorge=3120005412, Martha=3001234587)
print(movil)

del movil["Jorge"]
print(movil)
