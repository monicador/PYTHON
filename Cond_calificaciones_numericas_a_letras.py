'''
Desarrolle un algoritmo que permita convertir
calificaciones numéricas a letras, según la 
siguiente tabla: Se asume que la nota es un 
numero entero y está comprendida entre 1 y 20.

A = 19 y 20,
B = 16, 17  y 18 
C = 13, 14 y 15
D = 10, 11 y 12,
E =  1 hasta el  9.

'''

# ALGORITMO

nota = int(input("Diga la calificacion del estudiante: "))

if (nota >= 19) and (nota <= 20):
    nota = "A"
else:
    if (nota >= 16) and (nota <= 18):
        nota = "B"
    else: 
        if (nota >= 13) and (nota <= 15):
            nota = "C"
        else: 
            if (nota >= 10) and (nota <= 12):
                nota = "D"
            else:
                if (nota >= 1) and (nota <= 0):
                    nota = "E"
print("La calificacion del estudiante es: ", nota)







