'''
Pedir tres números y mostrarlos ordenados de mayor 
a menor; mostrar un mensaje de error en caso de 
ingresar dos o más números iguales.

Datos de entrada: 3 numeros
Proceso: Comprobacion de los numeros
Salidas: Los tres numeros ordenados de mayor a menor 
o mensaje de error por números iguales.

'''
# Iniciamos solicitando los tres numeros enteros.
print("Ingrese el primer numero: ")
num1 = int(input())
print("Ingrese el segundo numero: ")
num2 = int(input())
print("Ingrese el tercer numero: ")
num3 = int(input())
# Hacemos las comparaciones
if(num1>num2 and num2>num3):
    print("", num1, " - ",num2," - ", num3)
elif(num2>num1 and num1>num3):
    print("",num2," - ",num1," - ",num3)
elif(num3>num1 and num1>num2):
    print("", num3, " - ",num1," - ", num2)
elif(num3>num2 and num2>num1):
    print("", num3, " - ",num2," - ", num1)
elif(num1>num3 and num3>num2):
    print("", num1, " - ",num3," - ", num2)
elif(num2>num3 and num3>num1):
        print("", num2, " - ",num3," - ", num1)
else:
    print("Se ingresaron numeros iguales")







