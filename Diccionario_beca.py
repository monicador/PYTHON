def asignacion_becas(dicReporte: dict) -> dict:
    return dicReporte['estudiante']+" - "+"Tipo Beca: "+(dicReporte['tipoBeca'])
# Funcion para definir Beca de estudio

def definir_beca(datos_estudiante: dict) -> dict:
    if (datos_estudiante['promedio'] >= 3.5) and (datos_estudiante['estrato'] <= 2):
        beca = "La Beca incluye sostenimiento economico y el pago del 100 por ciento de los costos academicos"
    else:
        if (datos_estudiante['promedio'] == 3.5) and (datos_estudiante['estrato'] == 3):
            beca = "La Beca de estudio cubre el 40 por ciento de los costos academicos"
        else:
            if (datos_estudiante['promedio'] >= 4.0) and (datos_estudiante['estrato'] == 3):
                beca = "La Beca de estudio cubre el 70 por ciento de los costos academicos"
            else:
                if (datos_estudiante['promedio'] >= 4.0) and (datos_estudiante['estrato'] == 4):
                    beca = "La Beca de estudio cubre el 30 por ciento de los costos academicos"
                else:
                    beca = "No se otroga la beca"

    diccionario_respuesta = {
    "estudiante" : datos_estudiante['estudiante'], 
    "tipoBeca": beca
    }
    return diccionario_respuesta
# Prueba1
datos_estudiante = {
    "id_estudiante": "t001",
    "estudiante": "Sebastian Moreno",
    "promedio": 3.5,
    "estrato": 2
}
print(asignacion_becas(definir_beca(datos_estudiante)))
