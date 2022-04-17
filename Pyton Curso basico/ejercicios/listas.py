listaUno = ["Juan", 3, True, False, 0.12, "Ana"]
listaDos = ["Pedro", 2, 5, 4.435, False]
listaTres = []

# Formas de imprimir:
print(listaUno[:])
# ['Juan', 3, True, False, 0.12, 'Ana']
print(listaUno[:3])
# ['Juan', 3, True]
print(listaUno[2:])
# [True, False, 0.12, 'Ana']
print(listaUno[-3:])
# [False, 0.12, 'Ana']
print(listaUno[:-3])
# ['Juan', 3, True]
print(listaUno[1:5])
# [3, True, False, 0.12]

# Agregar un elemento al final:
listaUno.append("Manuel")
print(listaUno[:])
# ['Juan', 3, True, False, 0.12, 'Ana', 'Manuel']

# Agregar elemnto en otra posición:
listaUno.insert(3, "Daniela")
print(listaUno[:])

# Agregar varios elementos:
listaUno.extend([2, 10, "Gary"])
print(listaUno[:])

# Conocer indice del primer elemento encontrado:
print(listaUno.index("Manuel"))

# Buscar elemento en una lista:
estaElemento = "Manuel" in listaUno
print(estaElemento)

# Eliminar un  elemento:
listaUno.remove(False)
print(listaUno[:])

# Eliminar último elemento:
listaUno.pop()
print(listaUno[:])

# Unir dos listas:
listaTres = listaUno + listaDos
print(listaTres[:])

# Repetir elementos de una lista:
listaCuatro = [1, 2, 3] *4
print(listaCuatro[:])


