'''
Se desea calcular la distancia recorrida (m) por un movil que 
tiene velocidad constante (m/s) durante un tiempo T (sg), 
considerar que es un movimiento MRU (Movimiento Rectilineo uniforme)

ENTRADAS
Velocidad Constante V
Tiempo (sg)         T

PROCESOS
D = V * T

SALIDAS
Distancia Recorrida

'''
# Funcion que calcula la distancia recorrida

def distancia_recorrida(v, t):
    d = v * t
    return d

#Aqui inicia la aplicacion

v = int(input("Digite la velocidad: "))
t = int(input("Digite el tiempo: "))

distancia_recorrida = distancia_recorrida(v, t)
print("v * t =" , distancia_recorrida)