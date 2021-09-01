# Algoritmo de la suma de dos numeros

'''
Se desea la suma de dos numeros enteros y presentar en pantalla su resultado


ENTRADAS : Num1, Num2

PROCESO : LA SUMA DE LOS NUMEROS SUMA 

SALIDAS : LA SUMA DE LOS NUMEROS SUMA

INICIO
   Num1, Num2, Suma: Enteros
   ESCRIBA "Diga dos Numero:"
   LEA Num1, Num2
   Suma <-- Num1 + Num2
   ESCRIBA "La suma de los dos numeros es: ", suma 
   FIN

'''

# Suma dos Numeros
numero1 = int(input("Diga el primer numero: "))
numero2 = int(input ("Diga el segundo numero: "))

#Guarda el Resultado de la Suma de dos numeros
suma = numero1 + numero2

print("La suma de dos numeros es :", suma)

