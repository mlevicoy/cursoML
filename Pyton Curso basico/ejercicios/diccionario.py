miDiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}
miDiccionario2 = {"Alemania": 1945, 4:"Jordan", 1979:"Manuel"}

# Agregar una nueva clave:valor:
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)

# Modificar una clave:valor:
miDiccionario["Italia"] = "Roma"
print(miDiccionario)

# Eliminar una clave:valor:
del miDiccionario["Reino Unido"]
print(miDiccionario)

# Asignar valores de una tupla a un diccionario:
miTupla=("España", "Francia", "Reino Unido", "Alemania")
miDiccionario3 = {miTupla[0]:"Madrid", miTupla[1]:"París", miTupla[2]:"Londres", miTupla[3]:"Berlín"}
print(miDiccionario3)
print(miDiccionario3["Francia"])

# Diccionario con una tupla como valor:
miDiccionario4 = {
	23:"Jordan", 
	"Nombre":"Michael", 
	"Equipo":"Chicago", 
	"Anillos":(1991, 1992, 1993, 1996, 1997, 1998)
}
print(miDiccionario4)
print(miDiccionario4["Anillos"])

# Diccionario como un diccionario y una tupla como valor:
miDiccionario5 = {
	23:"Jordan", 
	"Nombre":"Michael", 
	"Equipo":"Chicago", 
	"Anillos":{
		"temporadas":(1991, 1992, 1993, 1996, 1997, 1998)
	}
}

# Obtener las claves:
print(miDiccionario.keys())

# Obtener los valores:
print(miDiccionario.values())

# Obtener la longitud:
print(len(miDiccionario))