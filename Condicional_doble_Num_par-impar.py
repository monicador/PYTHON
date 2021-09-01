
'''
Desarrolle un algoritmo que permita leer un valor cualquiera N 
y escriba si dicho numero es par o impar

Algoritmo
Inicio
    Digite un valor
    Si N es par entonces
        El numero es par
    Si NO
        El numero es impar
        Fin SI
Fin

'''

n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")

