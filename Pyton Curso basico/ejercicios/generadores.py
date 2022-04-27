def generaPares(limite):
	num = 1

	while num < limite:
		yield num * 2
		num = num + 1

devuelvePares = generaPares(10)

print(next(devuelvePares))

print("Código...")

print(next(devuelvePares))

print("Código...")

print(next(devuelvePares))

print("Código...")

print(next(devuelvePares))

# -------------------------------------------

def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		yield from elemento

ciudadesDevueltas = devuelveCiudades("Madrid", "Barcelona")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))



