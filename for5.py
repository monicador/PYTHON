'''
Estructura for 
una vez que el ciclo se interrumpe se ejecuta la
instrucción después de él. Por ejemplo:

La variable a inicia con el valor de (0)
Se ingresa al ciclo y se ejecuta (3) veces la instruccion

Luego se muestra en pantalla el valor de a es 3:
Explicación: For: Desde (0)- hasta (5)
'''

a = 0
for k in range(0, 5, 2):
    a += 1  # contador
    print("El valor de k es: ", k)

print("-------------------")
print("El valor de a es: "+str(a))

