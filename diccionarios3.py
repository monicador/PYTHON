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
