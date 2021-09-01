
# Ejemplo Promedio ventas de lunes a viernes 

def promedioVentas(dicVentas): #dicVentas en un Diccionario que
    sumatoria = 0 # Inicializo la variable sumatoria
    sumatoria += dicVentas['ventalunes']
    sumatoria += dicVentas['ventamartes']
    sumatoria += dicVentas['ventamiercoles']
    sumatoria += dicVentas['ventajueves']
    sumatoria += dicVentas['ventaviernes']

    promedio = round(sumatoria/5, 2)
    return promedio

# Creo el diccionario dicNotas = {}
dicVentas = {
    'ventalunes': 100000,
    'ventamartes': 250450,
    'ventamiercoles': 300800,
    'ventajueves': 330000,
    'ventaviernes': 410000,
}

print("El promedio de ventas de lunes a viernes es:", promedioVentas(dicVentas))
