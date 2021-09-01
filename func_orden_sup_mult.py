def multiplicacion(val1, val2):
    return (val1*val2)

# Esta es la funcion de orden superior
def operacion(funcion, val1, val2):
    print(funcion(val1, val2))

variable_multiplicacion = multiplicacion

resultado = operacion(variable_multiplicacion, 10, 5)
print(resultado)
