# usuario@dominio.xxx

arroba = 0
punto = 0

informacion = input("Ingrese su correo electrónico: ")
correo = informacion.lower()

for caracterCorreo in correo:
	if caracterCorreo == '@':
		arroba += 1
	elif caracterCorreo == '.':
		punto += 1

if arroba == 1 and punto >= 1:
	print(correo + ", es un correo válido.")
else:
	print(correo + ", no es un correo válido.")




