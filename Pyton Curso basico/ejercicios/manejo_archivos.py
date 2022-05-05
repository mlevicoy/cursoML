# Se importa la clase
from io import open

# Se habre el fichero para leer
archivo_texto = open("archivo.txt", "r")

archivo_texto.seek(len(archivo_texto.read())/2)

print(archivo_texto.read())





#print(archivo_texto.read())
#archivo_texto.seek(0)
#print(archivo_texto.read(11))





archivo_texto.close()

#archivo_texto.write("\n Siempre es una buena ocación para estudiar Python")

# Coloca línea por línea en una lista
#lineas_texto = archivo_texto.readlines()

# Cerramos el fichero
#archivo_texto.close()

#for i in lineas_texto:
#	print(i)

# Leemos el fichero
# texto = archivo_texto.read()

# Cerramos el fichero
# archivo_texto.close()

# print(texto)

# Se habre el fichero para escribir
# archivo_texto = open("archivo.txt", "w")

# frase = "Estupendo día para estudiar Python \n el miércoles."

# Escribimos en el fichero
# archivo_texto.write(frase)

# Cerramos el fichero
# archivo_texto.close()

