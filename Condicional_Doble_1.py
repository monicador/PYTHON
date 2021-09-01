'''
CONDIONAL DOBLE

Estructura Algoritmica de la condicional doble

Si <condición> entonces
              Acción(es) 
     si no
              Acción(es) 
Fin - Si

Determinar si un alumno aprueba o reprueba una 
asignatura, aprueba si el promedio de
tres calificaciones es mayor o igual a 3, 
en caso contrario reprueba.
'''

calificacion1 = float(input("Digite Calificacion 1: "))
calificacion2 = float(input("Digite Calificacion 2: "))
calificacion3 = float(input("Digite Calificacion 3: "))

promedio = (calificacion1+calificacion2+calificacion3)/3

if promedio >= 3:
      print("El alumno aprobo")
else:
      print("El alumno reprobo")


