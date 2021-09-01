'''
Pida al usuario la edad y el sexo, para que la computadora le 
indique si ya puede jubilarse. Tome en cuenta que un Hombre 
se puede jubilar cuando tenga 62 años o más, en cambio, 
una mujer mayor se jubilara si tiene más de 57 años.
'''

def Jubilacion(Sexo,Edad):
    if (Sexo == str("femenino")) and (Edad > 57):
        print ("Ya puede jubilarse")
    elif (Sexo == str("femenino")) and (Edad <= 57):
        print ("No puede jubilarse")
    elif (Sexo == str("masculino")) and (Edad > 62):
        print ("Ya puede jubilarse")
    elif (Sexo == str("masculino")) and (Edad <= 62):
        print ("No puede jubilarse")

Sexo = input("Diga si su sexo es femenino o masculino: ")
Edad = int(input("Diga su edad: "))
Jubil = Jubilacion(Sexo,Edad)

