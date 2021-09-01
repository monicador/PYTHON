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

N=int(input("ingrese tu nota\n"))
if(N == 19 or N == 20):
 print("Tu nota es A")
else:
 if(N <= 18 and N >= 16):
  print("Tu nota es B")
 else:
  if(N <= 15 and N >= 13):
   print("Tu nota es C")
  else:
   if(N <= 12 and N >= 10):
    print("Tu nota es D")
   else:
    if(N <= 9 and N >= 1):
     print("Tu nota es E")
    else:
     print("Esta fuera de rango(1 a 20)")
