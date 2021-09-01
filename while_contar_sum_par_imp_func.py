'''
Diseñe un algoritmo que permita contar y sumar los números pares e 
impares existentes en una serie de 1 a n, siendo n un número digitado por un usuario.
A) Imprimir Contador de impares y pares
B) Imprimir suma de impares y pares

'''

def contar (n):
    p = 0
    i = 0
    sumaPares = 0
    sumaImpares = 0
    while (n >= 1):
        if(n % 2 == 0):
            p += 1
            sumaPares = sumaPares + n
            n -= 1
        else:
            i += 1
            sumaImpares = sumaImpares + n
            n -= 1
    return[p, i, sumaPares , sumaImpares]

# Aqui inica el programa
numConteo = int(input("Ingrese numero hasta que quiera contar: "))

conteo = contar(numConteo)
print('cantidad de numero pares:', conteo[0] , ' \ncantidad de numero impares:', conteo[1])
print("suma pares : ",conteo[2], '\nsuma impares: ', conteo [3])

