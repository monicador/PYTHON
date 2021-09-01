'''
Diseñe un algoritmo que reciba numeros digitados por el usuario
y los imprima en pantalla, el programa debe terminar cuando el 
usuario digite un numero negativo '''

n = 0
while n>= 0:
    n = float(input("Digite un numero: "))
    if n >= 0:
        print("El numero digitado es: ", n)
        
