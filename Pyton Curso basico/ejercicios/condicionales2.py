edad = 7

if 0<edad<100:
 	print("Edad es correcta")
else:
 	print("Edad incorrecta")

# ---------------------------------------------------------------------------

salarioPresidente = int(input("Introducir salario presidente: "))
print("Salario presidente: " + str(salarioPresidente))

salarioDirector = int(input("Introducir salario director: "))
print("Salario director: " + str(salarioDirector))

salarioJefeArea = int(input("Introducir salario jefe de área: "))
print("Salario jefe de área: " + str(salarioJefeArea))

salarioAdministrativo = int(input("Introducir salario administrativo: "))
print("Salario administrativo: " + str(salarioAdministrativo))

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
	print("Todo esta correcto")
else:
	print("Error en salarios")

# ---------------------------------------------------------------------------

print("Programa de becas Año 2017")

distanciaEscuela = int(input("Intruducir la distancia a la escuela (KM): "))
print(distanciaEscuela)

numeroHermanos = int(input("Introducir el n° de hermanos en el centro: "))
print(numeroHermanos)

salarioFamilar = int(input("Introducir salario anual bruto: "))
print(salarioFamilar)

if (distanciaEscuela > 40 and numeroHermanos > 2) or salarioFamilar <= 20000:
	print("Tiene derecho a beca")
else:
	print("No tiene derecho a beca")

# ---------------------------------------------------------------------------

print("Asignaturas optativas año 2017")
print("Asignaturas optativas: matemáticas, lenguaje, ingles, portugues, ciencias")
asignatura = input("Escriba la asignatura escogida: ")

if asignatura.lower() in ("matemáticas", "lenguaje", "ingles", "portugues", "ciencias"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura escogida no está contemprada")


