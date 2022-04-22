# Ejercicio 1

print("Ejercicio 1\n")
numeroUno = int(input("Ingresar primer número: "))
numeroDos = int(input("Ingresar segundo número: "))

def DevuelveMax(num1, num2):
	if num1 > num2:
		return num1
	elif num1 < num2:
		return num2
	else:
		return "Error: Los números son iguales"

print("El número mayor entre " + str(numeroUno) + " y " + str(numeroDos) + " + es: " + str(DevuelveMax(numeroUno, numeroDos)) + "\n")

# Ejercicio 2

print("\nEjercicio 2\n")

nombre = input("Ingresar su nombre: ")
direccion = input("Ingresar su dirección: ")  
telefono = int(input("Ingresar su número de telefono:"))

lista = []

lista.append(nombre)
lista.append(direccion)
lista.append(telefono)

print(lista)
