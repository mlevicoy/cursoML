nombreUsuario = input("Introduce tu nombre de usuario: ")

print("El nombre es: ", nombreUsuario.upper())
print("El nombre es: ", nombreUsuario.lower())
print("El nombre es: ", nombreUsuario.capitalize())
print("La letra a, aparece ", nombreUsuario.count("a"), " veces")
print("El caracter a, aparece en la posición: ", nombreUsuario.find("a"))
print("El texto ingresado es (True) número o no (False): ", nombreUsuario.isdigit())
print("El texto ingresado es (True) alfanumérico o no (False): ", nombreUsuario.isalnum())
print("El texto ingresado tiene (True) solo letras o no (False): ", nombreUsuario.isalpha())
print("El nombre separado por espacio: ", nombreUsuario.split(" "))
print("Quitando espacios al principio y fin: ", nombreUsuario.strip())
print("Reemplazamos la palabra Ana por Daniela: ", nombreUsuario.replace("Ana", "Daniela"))
print("El caracter a, aparece en la posición (desde atrás): ", nombreUsuario.rfind("a"))


