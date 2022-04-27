def suma(num1, num2):
	return num1 + num2

def resta(num1, num2):
	return num1 - num2

def multiplica(num1, num2):
	return num1 * num2

def divide(num1, num2):
	try:
		return num1 / num2
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operación errónea"

while True:
	try:
		op1 = (int(input("Introduce el primer número: ")))
		op2 = (int(input("Introduce el segundo número: ")))
		break
	except ValueError:
		print("Los valores introducidos no son correctos. Inténtalo de nuevo.")

operacion = (input("Introduce la operación a realizar (suma, resta, multiplica, divide): "))

if operacion == "suma":
	print(suma(op1, op2))

elif operacion == "resta":
	print(resta(op1, op2))

elif operacion == "multiplica":
	print(multiplica(op1, op2))

elif operacion == "divide":
	print(divide(op1, op2))

else:
	print("operación no contemplada")

# ------------------------------------------------------------------

def dividiendo():
	while True:
		try:
			op1 = (float(input("Introduce el primer número: ")))
			op2 = (float(input("Introduce el segundo número: ")))
			print("La división es: " + str(op1/op2))
			break
		except ValueError:
			print("El valor introducido es errónea")
		except ZeroDivisionError:
			print("No se puede dividir entre 0!")
		finally:
			print("Cálculo finalizado")

dividiendo()

# ------------------------------------------------------------------

import math

def calculaRaiz(num1):
	if num1 < 0:
		raise ValueError ("El número no puede ser negativo.")
	else:
		return math.sqrt(num1)

op1 = (int(input("Introduce un número: ")))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print("Programa terminado")

# Tabnine

