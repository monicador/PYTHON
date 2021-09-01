'''
Diseñe un algoritmo que permita contar y sumar los números pares 
e impares existentes en una serie de 1 a n, 
siendo n un número digitado por un usuario. 

A) Imprimir Contador de impares y pares.
B) Imprimir Suma de impares y pares.
'''

'''def contar_pares_impares(lista):
    pares, impares = 0,0

    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares'''
tamaño = int(input("ingrese el tamaño de la lista "))
lista=[]
for i in range(0, tamaño): 
    lista.append(input("ingrese el numero de la lista "))


print(lista)
'''resultado = contar_pares_impares(numeros)

print("La cantidad de pares es: %i" % resultado [0])
print("La cantidad de impares es: %i" % resultado [1])'''







