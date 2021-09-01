'''
CONDICIONAL DOBLE
Diseñar un algoritmo que imprima el nombre del
articulo, código, precio y precio con descuento.
Si el articulo tiene código 01, el descuento es
del 10%, si el código es diferente el
Descuento es del 20% (solo existen dos articulos).

ALGORITMO
Inicio
     precio,precio_desc: float
     LEER nom_articulo, codigo, precio
    Si codigo  = 01 entonces      
           precio_desc = precio-precio*0.10
        Si No
           precio_desc = precio-precio*0.20
     Fin Si
     imprimir nom_articulo,codigo,
                         precio,precio_desc 
Fin

'''
print('\n')
cod_articulo = input("Digite Codigo del Articulo: ")
nom_articulo = input("Digite Nombre del Articulo: ")
precio = float(input("Digite precio del Articulo: "))

if cod_articulo == "01":
    precio_desc = precio-precio*0.10
else:
    precio_desc = precio-precio*0.20

print('\n')
print("Codigo Articulo: ", cod_articulo )
print("Nombre Articulo: ", nom_articulo )
print("Precio Articulo: ", precio)
print("Precio Articulo con Descuento: ", precio_desc)
print('\n')



