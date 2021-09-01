'''
A un trabajador se le paga por sus horas trabajadas y la tarifa por hora, 
si la cantidad de horas es mayor a 40 entonces el costo por la hora extra 
será un 50% adicional a la tarifa por hora, calcular el salario total del trabajador.

'''
tarifa = int(input("Ingrese la tarifa por horas "))
horas = int(input("Ingrese las horas trabajadas "))
salario = tarifa*horas
horasextras = horas-40
extras = (40*tarifa)+(horasextras*tarifa*1.5)
if horas>40:
    print("El salario es: S/", extras)
else:
    print("El salario es: S/", salario)
