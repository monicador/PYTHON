'''
Capturar por teclado 5 numeros y realiza la sumatoria de los mismos,
al final imprime la sumatoria de los numeros digitados
'''


total = 0
for i in range(5):
    nuevoNumero = int(input("Introduce un numero: "))
    total += nuevoNumero
    print("El total es: ", total)
