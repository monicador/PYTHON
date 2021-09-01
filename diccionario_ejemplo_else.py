'''

Calcular la utilidad que un trabajador recibe en el
reparto anual de utilidades si este se le asigna como
un porcentaje de su salario mensual que depende de su
antigüedad en la empresa de acuerdo con la siguiente

Tabla:

------------------------------------------------------------
Tiempo                                    Utilidad
------------------------------------------------------------
Menos de 1 año                        5% del salario
1 año o más y menos de 2 años         7% del salario
2 años o más y menos de 5 años        10% del salario
5 años o más y menos de 10 años       15% del salario
10 años o más                         20% del salario
-----------------------------------------------------------
'''
def asignacion_utilidad(dicReporte: dict) -> dict:
    return dicReporte['trabajador']+" - "+"tipo incremento: "+(dicReporte['tipoincremento'])
# Funcion para definir el tipo de incremento

def definir_incremento(datos_trabajador: dict) -> dict:
    if (datos_trabajador['antiguedad'] > 1):
        incremento = "Tiene derecho a un incremento del 5 por ciento del salario"
    else:
        if (datos_trabajador['antiguedad'] >= 1) and (datos_trabajador['antg']<2):
            incremento = "Tiene derecho a un incremento del 7 por ciento del salario"
        else:
            if (datos_trabajador['antiguedad'] >= 2) and (datos_trabajador['antig']>5):
                incremento = "Tiene derecho a un incremento del 10 por ciento del salario"
            else:
                if (datos_trabajador['antiguedad'] >= 5) and (datos_trabajador['antig']<10):
                    incremento = "Tiene derecho a un incremento del 15 por ciento del salario"
                else:
                    incremento = incremento = "Tiene derecho a un incremento del 20 por ciento del salario"

    diccionario_respuesta={
        'trabajador': datos_trabajador['trabajador'],
        'tipoincremento': incremento
    }
    return diccionario_respuesta

# Prueba1
datos_trabajador = {
    "id_trabajador": "t001",
    "trabajador": "Luis Moreno",
    "incremento": 15,
    "antiguedad": 8
}
print(asignacion_utilidad(definir_incremento(datos_trabajador)))
print('\n')

