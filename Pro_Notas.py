

'''

Se necesita obtener el promedio de tres notas parciales de la asignatura Inglés, 
muestre por pantalla el promedio de dichas calificaciones:

a. Construir Algoritmo, pero antes de esto identificar las entradas, el proceso 
necesario para calcular promedio de Notas y salida

Entradas: nota1, nota2, nota3
Proceso: Promedio = (nota1 + nota2+ nota3)/3
Salidad: promedio

Algoritmo
Inicio
    Leer nota1
    Leer nota2
    Leer nota3

  Promedio = (n1  + n2 + n3)/3
    Escribe promedio
Fin
'''


def calcular_promedio_notas(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3)/3
    return promedio

print('/n')
n1 = int(input("Diga la primera nota del curso de Ingles: "))
n2 = int(input("Diga la segunda nota del curso de Ingles: "))
n3 = int(input("Diga la tercera nota del curso de Ingles: "))

prom = calcular_promedio_notas(n1, n2, n3)

print("La nota promedio del curso de Ingles es: %2f"% prom)
print('/n')