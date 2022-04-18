miTupla = ("Juan", 13, 13, 1, 1995)
miTupla4 = ("juan", 13, 1, 1995)
miLista = ["Diego", 22, 44, 3333]

# Pasar de tupla a lista
lista = list(miTupla)
print(lista)

# Pasar de lista a tupla
tupla = tuple(miLista)
print(tupla)

# Ver si un elemento esta en una tupla
esta = "Juan" in miTupla
print(esta)

# Ver cuantas veces se repite un elemento en una tupla
cuantasVeces = miTupla.count(13)
print(cuantasVeces)

# Ver cuantos elementos hay
cuantosElementos = len(miTupla)
print(cuantosElementos)

# Tupla unitaria, debe ir con coma al final
miTupla2 = ("Juan",)
print(miTupla2)

# Las tupla pueden ir sin parentesis
miTupla3 = "Juan", 13, 13, 14, 1, 1995
print(miTupla3)

# desempaquetado de tuplas
nombre, dia, mes, anho = miTupla4
print(nombre)
print(dia)
print(mes)
print(anho)


