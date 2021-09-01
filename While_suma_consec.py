'''Realizar un algoritmo para sumar consecutivamente 
y cuando la suma sea superior a 100 
deje de pedir números y muestre el total.'''

suma = 0
numero = 0

while suma <=100:
    numero = int(input("Escriba un numero: "))
    suma = suma + numero
print(("Total de la suma da: "), round(suma))