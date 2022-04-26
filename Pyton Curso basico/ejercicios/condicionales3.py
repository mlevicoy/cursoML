import math

print("Programa de calculo de raíz cuadrada")
numero = int(input("Introduce un número por favor: "))

intentos = 0

while numero < 0:
	print("No se puede hallar la raíz de un número negativo")
	if intentos == 2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break;

	numero = int(input("Introduce un número por favor: "))
	if numero < 0:
		intentos = intentos + 1

if intentos < 2:
	solucion = math.sqrt(numero)
	print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))

# ---------------------------------------------------------------------------------

#Ejercicio 1

print("Ejercicio N°1")

numeroUno = int(input("Ingresar número: "))
numeroDos = int(input("Ingresar número: "))

while numeroDos > numeroUno:
	numeroUno = numeroDos
	numeroDos = int(input("Ingresar número: "))

print("El flujo ha finalizado, agrego un número menor.")

# ---------------------------------------------------------------------------------

#Ejercicio 2

print("Ejercicio N°2")

numero = int(input("Ingresar número positivo: "))
lista = []

while numero >= 0:
	lista.append(numero)
	numero = int(input("Ingresar número positivo: "))	

suma = sum(lista)
print("Programa finalizado, la suma de los número positivos es: " + str(suma))

suma2 = 0
for i in lista:
	suma2 = suma2 + i
print("Programa finalizado, la suma de los número positivos es: " + str(suma2))

# ---------------------------------------------------------------------------------

email = input("Introduce tu email, por favor: ")
for i in email:
	if i == "@":
		arroba = True
		break;
else:
	arroba = False
print(arroba)









