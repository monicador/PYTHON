def division(val1, val2):
    return (val1/val2)

# Esta es la funcion de orden superior
def operacion(funcion, val1, val2):
    print(funcion(val1, val2))

variable_division = division

resultado = operacion(variable_division, 10, 5)
print(resultado)
