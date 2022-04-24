print("Programa de evaluación de notas de alumnos")
#nota_alumno = input("Introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion = "Aprobado"
	if nota < 5:
		valoracion = "Reprobado"
	return valoracion

#print(evaluacion(int(nota_alumno)))

print("Programa permiso usuario por edad")
edad = int(input("Ingrese su edad: "))

def validar(edad):		
	if edad > 100:
		permiso = "Edad incorrecta"
	elif edad >= 18:
		permiso = "Se permite el acceso"
	else:
		permiso = "No se permite el acceso"
	return permiso

print(validar(edad))


