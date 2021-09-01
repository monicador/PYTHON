'''
count()
Este metodo recibe un elemento como argumeto, y cuenta la cantidad de 
veces que aparece en la tupla.
'''
valores = ("Uva", True, "Avion", 10)
print("La palabra Uva aparece en la Tupla : ", valores.count("Uva"))

# Acceso a los elementos usando un indice negativo
frutas =  ("Uva", "Lulo", "Naranja", "Mango")
frutas[-1] # Mango

# Acceso a un subconjunto de elementos
vocales = "a", "e", "i", "o", "u"
vocales[2:3] # Elementos desde el indice 2 hasta el indice 3-1 (i)
vocales[2:4] # Elementos desde el indice 2 hasta el indice 4-1 (i, o)
vocales[:] # Todos los elementos

