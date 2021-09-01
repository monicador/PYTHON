'''
El método dict() de los Diccionarios recibe como parametro 
una representacion de un diccionario y devuelve un diccionario de datos

'''
# EJEMPLO 1
factura = dict(nrofactura=8954, valor=150000, iva=True)

print(factura)

print(factura['valor'])
print(factura['iva'])



# EJEMPLO2
#ALGUNOS EJEMPLOS ********
'''
Podemos obtener todas las llaves de nuestro diccionario
utilizando el metodo keys()

'''
empleados = {'Sandra': 1, 'Teresa': 2, 'Juan': 2}
print(empleados.keys())

# El Método items() devuelve una lista de clave: valor del diccionario
empleados = {'Sandra': 1, 'Teresa':2, 'Juan': 2}
print(empleados.items())

# EJEMPLO DE UNA FUNCION
# La funcion len() cuenta el numero de llaves del diccionario
empleados = {'Sandra': 1, 'Teresa': 2, 'Juan': 2}
print(len(empleados))

# PASANDO INFORMACION A TRAVES DE DICCIONARIOS
'''
Los diccionarios ofrecen la posibilidad de empaquetar
o encapsular varias varibles para facilitar el envio de
parámetros.
'''
# Encapsulamiento con Diccionario
# Ejemplo
def promedioNotas(dicNotas): #dicNotas en un Diccionario que
    sumatoria = 0 # Inicializo la variable sumatoria
    sumatoria += dicNotas['nota1']
    sumatoria += dicNotas['nota2']
    sumatoria += dicNotas['nota3']
    promedio = round(sumatoria/3, 2)
    return promedio

# Creo el diccionario dicNotas = {}
dicNotas = {
    'nota1': 2.5,
    'nota2': 3.5,
    'nota3': 4.5
}

print("El promedio es:", promedioNotas(dicNotas))


